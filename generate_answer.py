from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch import Tensor

"""
   Attributes:

    tokenizer: GPT2Tokenizer
       Tokenizer for input text
    model: GPT2LMHeadModel
       Trained a neural network to generate text
    max_length : int
       Maximum length of generated text
    repetition_penalty : float
       Used to punish words that have already been created or belong to the context
    top_k : int
       In Top-K sampling, the K most likely next words are filtered and the probability mass is redistributed
           among only those K next words.
    top_p : float
       Top-p sampling chooses from the smallest possible set of words whose cumulative probability exceeds
           the probability p. The probability mass is then redistributed among this set of words.
    temperature: float
       increasing the likelihood of high probability words and decreasing the likelihood of low probability words
           by lowering the so-called temperature of the softmax.
   Methods
   -------
   generate_simple_answer(text, max_length: int, repetition_penalty: float, top_k: int,
                           top_p: float, temperature: float)
       Generates a continuation for the given text
   """

def generate_simple_answer(text, max_length: int, repetition_penalty: float, top_k: int,
                           top_p: float, temperature: float):
    model_name_or_path = "models/essays"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
    model = GPT2LMHeadModel.from_pretrained(model_name_or_path)
    input_ids = tokenizer.encode(text, return_tensors="pt", )
    out = model.generate(input_ids, max_length=max_length, repetition_penalty=repetition_penalty,
                         top_k=top_k, top_p=top_p, temperature=temperature)
    generated_text = list(map(tokenizer.decode, out))[0]
    print(generated_text)
    return generated_text

if __name__ == "__main__":
    text = generate_simple_answer("Тест", 100, 5.0, 10, 0.95, 1)