# study_LangGraph

* LangGraphの学習メモ用repository
* 『LangChainとLangGraphによるRAG・AIエージェント実践入門（西田公宏）』書籍の学習内容をまとめる

## notebook内容
* 01_about_LangGraph.ipynb
  * LangGraphの概念・用語など
* 02_LangGraph_sample_code_1.ipynb
  * LangGraphにより基本的なマルチエージェント構築例
* 03_about_CheckPoint.ipynb
  * チェックポイントについて
* 04_make_requirements_definition_agent.ipynb
  * マルチエージェント構築例2
* 13_ChainsLangGraph.ipynb
  * リデューサーとツール呼び出しの基本（ToolNodeの利用）
* 14_chatbotswithmultipletools.ipynb
  * 複数ツールの利用（最適なツールを一つ選択して実行）
* 15_ReActAgents.ipynb
  * React型エージェントとメモリ機能について（`create_react_agent`関数を使わない版）
* 09_create_react_agent_func.ipynb
  * ツールの呼び出しを伴うAIエージェント作成用関数
* 16_streaming.ipynb
  * ストリーム出力について
* 22_Humanintheloop.ipynb
  * ヒューマンフィードバックの適用

### Agentic RAG
* 23_AgenticRAG.ipynb
  * エージェントによる最適なベクトルDBの選択
* 24_CorrectiveRAG.ipynb
  * ベクトル検索結果に対するセルフリフレクションの適用
* 25_AdaptiveRAG.ipynb
  * クエリ内容を分析して、動的にRAGのクエリを最適化

### エージェントデザインパターン
* 05_about_agent_design_pattern.ipynb
  * 主要なエージェントデザインパターンの解説
* 06_Passive_Goal_Creator.ipynb
  * ユーザーからの具体的な目標を抽出するパターンの構築例
* 07_Prompt_Response_Optimizer.ipynb 
  * 生成された目標やユーザー要求を、より効果的なプロンプトに変換しLLMからより質の高い回答を得るパターンの構築例
* 08_Single-Path_Plan_Generator.ipynb
  * 設定された目標を達成するための一連の具体的なステップを生成するパターンの構築例
* 10_Multi-Path_Plan_Generator.ipynb
  * タスク分解時に複数の選択肢を同時に生成し、実行時のコンテキストに応じて実行エージェント自身に都度適切な選択をさせるパターンの構築例
* 11_Self-Reflection_and_Cross-Reflection.ipynb
  * タスクの実行結果をエージェント自身で振り返ることで、その実行内容を自己改善させるの構築例
* 12_Role-Based_Cooperation.ipynb
  * AIエージェントが協調してタスク実行の構築例
* 17_prompting_chaining.ipynb
  * サブクラスに分解して順番に処理する構築例
* 18_parallelization.ipynb
  * 複数ノードが独立して動くことができるときに、並列化を適用する例
* 19_Routing.ipynb
  * 条件分岐による様々なノードへのルーティング
* 20_orchestrator-worker.ipynb
  * 管理エージェントがサブタスクに分解して、作業用エージェントに依頼する例
* 21_Evaluator-optimizer.ipynb
  * LLM出力結果を評価用LLMが評価する例

### アプリ
* 26_LangGraph_app_with_Streamlit/
  * Streamlitを利用したLangGraphによるレポート生成アプリ
