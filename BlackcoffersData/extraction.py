import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
nltk.download()

from nltk.corpus import stopwords
stopwords.words()

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Load the extracted data from extracted_data.xlsx
extracted_data_path = r'C:\Users\User\Downloads\extracted_data.xlsx'
extracted_df = pd.read_excel(extracted_data_path)

def compute_variables(text):
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Compute variables
    word_count = len(tokens)
    filtered_word_count = len(filtered_tokens)
    avg_sentence_length = word_count / text.count('.') 
    percentage_complex_words = (filtered_word_count / word_count) * 100
    
    # Perform sentiment analysis
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    return {
        'Word_Count': word_count,
        'Filtered_Word_Count': filtered_word_count,
        'Avg_Sentence_Length': avg_sentence_length,
        'Percentage_Complex_Words': percentage_complex_words,
        'Polarity_Score': polarity_score,
        'Subjectivity_Score': subjectivity_score
    }

# Compute variables
variable_data = []
for index, row in extracted_df.iterrows():
    article_text = row['Article_Text']
    variables = compute_variables(article_text)
    variable_data.append(variables)

variable_df = pd.DataFrame(variable_data)

output_df = pd.concat([extracted_df, variable_df], axis=1)

# Save the output DataFrame
output_file_path = r'C:\Users\User\Downloads\output_data_structure.xlsx'
output_df.to_excel(output_file_path, index=False)