from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)

@app.route('/')
def home():
    return 'Instagram downloader is running!'

@app.route('/api', methods=['GET'])
def download_instagram_video():
    url = request.args.get('url')
    if not url:
        return jsonify({'status': 'error', 'message': 'URL is missing'})

    L = instaloader.Instaloader()
    sessionid = '73394703601%3AJ9E4cS9whE7pQ5%3A2%3AAYf8u6aehuRKRY22DAXDBjSV9GjAtQq_ZzqZKyAGtQ'  # Replace with your sessionid
    L.context._session.cookies.set('sessionid', sessionid, domain='.instagram.com')

    try:
        shortcode = url.split('/reel/')[1].split('/')[0]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        video_url = post.video_url
        thumbnail_url = post.url  # This is the thumbnail image

        return jsonify({
            'status': 'success',
            'video_url': video_url,
            'thumbnail_url': thumbnail_url
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
