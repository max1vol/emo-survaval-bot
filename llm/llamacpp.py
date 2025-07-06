from llama_cpp import Llama

print("Loading...")
llm = Llama.from_pretrained(
    repo_id="ggml-org/gemma-3-1b-it-GGUF", filename="*Q4_K_M.gguf", verbose=False
)
print("Running inference...")
output = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {"role": "user", "content": "Hello, how are you?"},
    ]
)
print(output)
