# Streamlitを用いたLangGraphアプリ

### 以下の機能を持つLangGraphアプリ実装例
* チャット
* webサーチによるグラウンディング
* AIニュースに関する、daily, weekly, monthlyレポートの自動作成

`streamlit run app.py`にて起動  

### フォルダ構成
app.py - プログラム実行用ファイル  
src/  
 └ langgraphagenticai/  
    └ main.py - LangGraph定義・呼び出し用ファイル   
    └ graph/  
       └ graph_builder.py - グラフ定義クラス  
    └ LLMS/  
       └ gptllm.py - LLM定義クラス  
    └ nodes/  
       └ ai_news_nodes.py - aiによるニュース作成用node定義クラス  
       └ basic_chatbot_node.py - チャットボット用node定義クラス  
       └ chatbot_with_Tool_node.py - チャットボットによるweb検索用node定義クラス  
    └ state/  
       └ state.py - ステート定義クラス  
    └ tools  
       └ search_tool.py - webサーチ用ツール定義  
    └ ui  
       └ uiconfigfile.ini - ui用初期設定用ファイル  
       └ uiconfigfile.py - 初期設定読み込み用  
       └ streamlit/  
          └ display_result.py - LLM生成結果出力用  
          └ load_ui.py - 入力画面用  
AINews/ - 出力されたレポート保存用フォルダ  
