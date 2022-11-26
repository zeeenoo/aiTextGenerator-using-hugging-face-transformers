from transformers import pipeline


summarizer = pipeline('summarization')

article =input('enter the text that  u want to summarize it')

minLength= int(input('enter the min length '))
maxLength= int(input('enter the max length '))
summarizedText = summarizer(article,max_length=maxLength,min_length=minLength,do_sample=False)

print(summarizedText)
