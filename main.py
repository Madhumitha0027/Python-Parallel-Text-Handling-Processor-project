from database.db_manager import create_table, insert_result
from modules.text_loader import split_text, parallel_process
from modules.rule_engine import calculate_sentiment

# 🔥 multiprocessing kosam TOP LEVEL function
def process_chunk(chunk):
    score, tag = calculate_sentiment(chunk)
    insert_result(chunk, score, tag)

# 🔥 VERY IMPORTANT (Windows multiprocessing fix)
if __name__ == "__main__":

    create_table()

    # sample text (testing kosam)
    text = """
    Today is a good day. I feel happy.
    Sometimes coding gives error and makes me sad.
    But learning is excellent and I love solving problems.
    """

    chunks = split_text(text)

    # 🔥 TRUE MULTIPROCESS EXECUTION
    parallel_process(chunks, process_chunk)

    print("Processing Completed!")