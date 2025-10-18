from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
import sys
import os
import traceback
import tempfile

debug_bp = Blueprint('debug', __name__)

@debug_bp.route('/debug/info', methods=['GET'])
@cross_origin()
def debug_info():
    """デバッグ情報を返すエンドポイント"""
    try:
        import requests
        import bs4
        import markdownify
        import zipfile
        
        return jsonify({
            'status': 'ok',
            'python_version': sys.version,
            'python_path': sys.path,
            'current_working_directory': os.getcwd(),
            'temp_directory': tempfile.gettempdir(),
            'environment_variables': {
                'PATH': os.environ.get('PATH', 'Not set'),
                'PYTHONPATH': os.environ.get('PYTHONPATH', 'Not set'),
            },
            'modules': {
                'requests': requests.__version__,
                'bs4': bs4.__version__,
                'markdownify': getattr(markdownify, '__version__', 'version not available'),
            }
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e),
            'traceback': traceback.format_exc()
        }), 500

@debug_bp.route('/debug/test-request', methods=['POST'])
@cross_origin()
def test_request():
    """リクエストの詳細をテストするエンドポイント"""
    try:
        # リクエストの詳細情報を取得
        request_info = {
            'method': request.method,
            'url': request.url,
            'headers': dict(request.headers),
            'content_type': request.content_type,
            'is_json': request.is_json,
            'data': None,
            'json': None
        }
        
        # データの取得を試行
        try:
            if request.is_json:
                request_info['json'] = request.get_json()
            else:
                request_info['data'] = request.get_data(as_text=True)
        except Exception as data_error:
            request_info['data_error'] = str(data_error)
        
        return jsonify({
            'status': 'ok',
            'message': 'Request received successfully',
            'request_info': request_info
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e),
            'traceback': traceback.format_exc()
        }), 500

@debug_bp.route('/debug/simple-download', methods=['POST'])
@cross_origin()
def simple_download():
    """簡単なダウンロードテスト"""
    try:
        import requests
        from bs4 import BeautifulSoup
        
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': 'URLが指定されていません'}), 400
        
        url = data['url']
        
        # 単純なHTTPリクエストのテスト
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # HTMLの解析テスト
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find('title')
        title = title_tag.get_text().strip() if title_tag else 'No title found'
        
        return jsonify({
            'status': 'ok',
            'message': 'Simple download test successful',
            'url': url,
            'status_code': response.status_code,
            'content_length': len(response.content),
            'title': title
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e),
            'traceback': traceback.format_exc()
        }), 500

