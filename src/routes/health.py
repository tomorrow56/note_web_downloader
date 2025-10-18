from flask import Blueprint, jsonify
from flask_cors import cross_origin

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
@cross_origin()
def health_check():
    """ヘルスチェック用エンドポイント"""
    try:
        import requests
        import bs4
        import markdownify
        import tempfile
        import zipfile
        
        return jsonify({
            'status': 'ok',
            'message': 'All dependencies are available',
            'dependencies': {
                'requests': 'ok',
                'bs4': 'ok', 
                'markdownify': 'ok',
                'tempfile': 'ok',
                'zipfile': 'ok'
            }
        }), 200
    except ImportError as e:
        return jsonify({
            'status': 'error',
            'message': f'Missing dependency: {str(e)}',
            'dependencies': {}
        }), 500
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Health check failed: {str(e)}',
            'dependencies': {}
        }), 500

@health_bp.route('/test-download', methods=['POST'])
@cross_origin()
def test_download():
    """ダウンロード機能のテスト用エンドポイント"""
    try:
        from flask import request
        import tempfile
        import os
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        url = data.get('url', 'https://qiita.com/Qiita/items/c686397e4a0f4f11683d')
        
        # 一時ディレクトリのテスト
        temp_dir = tempfile.mkdtemp()
        test_file = os.path.join(temp_dir, 'test.txt')
        
        with open(test_file, 'w') as f:
            f.write('test content')
            
        file_exists = os.path.exists(test_file)
        
        # クリーンアップ
        os.remove(test_file)
        os.rmdir(temp_dir)
        
        return jsonify({
            'status': 'ok',
            'message': 'Test download endpoint working',
            'url_received': url,
            'temp_dir_test': 'passed' if file_exists else 'failed'
        }), 200
        
    except Exception as e:
        import traceback
        return jsonify({
            'status': 'error',
            'message': str(e),
            'traceback': traceback.format_exc()
        }), 500

