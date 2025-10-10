import openai

# OpenAI clientを初期化
client = openai.OpenAI(api_key="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")

# テスト用のプロンプト
prompt_text = "あなたはアンケートで誠実な回答を促すためのメッセージを生成するAIです。行動経済学のナッジ理論にもとづき、不誠実回答者を減らすメッセージを考えてください。"

try:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": "100字以内でメッセージを生成してください。"}
        ],
        max_tokens=100
    )
    
    # 生成されたメッセージを表示
    generated_text = response.choices[0].message.content.strip()
    print("生成されたメッセージ:")
    print(generated_text)
    print("\nAPI呼び出しが正常に完了しました。")
    
except Exception as e:
    print(f"Error calling OpenAI API: {e}")