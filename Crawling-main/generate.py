from transformers import T5ForConditionalGeneration, T5Tokenizer


class Generate:
    def __init__(self, model_url):
        self.model = T5ForConditionalGeneration.from_pretrained(model_url)
        self.tokenizer = T5Tokenizer.from_pretrained(model_url)

    def generate_text(self, text):
        text = 'summarize :'+text
        ids = self.tokenizer.encode(text, return_tensors='pt')
        generate = self.model.generate(ids)
        return self.tokenizer.decode(generate[0])

    def input_generate(self, df, column):
        dataframe = df.copy()
        dataframe['generated_text'] = dataframe['document'].apply(lambda x: self.generate_text(x))
        return dataframe
