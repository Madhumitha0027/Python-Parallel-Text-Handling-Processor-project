from concurrent.futures import ProcessPoolExecutor

def split_text(text, size=200):
    chunks = []
    for i in range(0, len(text), size):
        chunks.append(text[i:i+size])
    return chunks

def parallel_process(chunks, process_function):
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(process_function, chunks)
