# Discussions: Evolution of the Log Extraction Script

## Initial Basic Implementation

### What It Did:
The first version of the script read the log file line by line and checked if each line started with the target date. If it matched, it wrote the line to the output file.

### Key Points:
- **One Line at a Time**: The script processed each line one by one.
- **Single Thread**: It only used one thread, so it was slow for large files.
- **Direct Write**: Every matching line was written immediately to the output file.

### Pros:
- **Simple**: Easy to write and understand.
- **Low Memory**: Only one line was handled at a time.

### Cons:
- **Very Slow**: Processing large files (like 1TB) took too long.
- **Too Many Writes**: Writing each line to the file increased the time.
- **Not Scalable**: Couldn’t handle large workloads well.

---

## Final Multithreading Implementation

### What Changed:
This version used multithreading. The file was divided into chunks, and each chunk was processed by a separate thread to speed things up.

### Key Points:
- **Chunk Processing**: The file was split into chunks, and threads processed these chunks in parallel.
- **Threads with Executor**: Multiple threads worked together to process the file.
- **Direct Write per Thread**: Each thread wrote matching lines to the output file.

### Pros:
- **Faster**: Using multiple threads made it quicker than the single-threaded version.
- **Better File Reading**: Reading chunks was faster than reading line by line.
- **Parallel Processing**: Tasks were divided among threads.

### Cons:
- **Thread Overhead**: Managing threads added a bit of extra work.
- **Python GIL Limitation**: Threads couldn’t fully use CPU power for heavy tasks.
- **Writing Bottleneck**: Many threads writing to the same file slowed things down.
