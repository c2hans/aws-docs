---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/troubleshooting.html
---

# Troubleshooting code generation scenarios in Amazon Q Developer
<a name="troubleshooting"></a>

You might encounter the following common scenarios with inaccurate code generation and resolutions when using Amazon Q Developer:
+ [Empty code generation](#suggestions-troubleshooting)
+ [Continuous comments](#comments-troubleshooting)
+ [Incorrect in-line code generation](#code-generation-troubleshooting)
+ [Inadequate results from chats](#chat-results-troubleshooting)

## Empty code generation
<a name="suggestions-troubleshooting"></a>

While developing code, you might notice the following issues:
+ Amazon Q does not provide a suggestion.
+ The message "No Suggestion from Amazon Q" appears in your IDE.

Your first thought might be that Amazon Q isn't working properly. However, the root cause of these issues is typically associated with the context in the script or open project within the IDE.

If Amazon Q Developer doesn't provide a suggestion automatically, you can use the following shortcuts to manually execute Amazon Q in-line suggestions:
+ PC** **- **Alt\+C**
+ MacOS - **Option\+C**

For more information, see [Using shortcut keys](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/actions-and-shortcuts.html) in the *Amazon Q Developer User Guide*.

In most scenarios, Amazon Q generates a suggestion. When Amazon Q returns a "No Suggestion from Amazon Q" message, review the following common resolutions for this issue:
+ **Inadequate context** – Make sure that applicable libraries are present. Make sure that classes and functions defined in the script relate to new code.
+ **Ambiguous prompt** – If the prompt is confusing or unclear, Amazon Q will underperform when it makes in-line code suggestions. In these scenarios, be more specific in your code and comments to elicit proper responses.

If you're stuck, continue coding to the best of your ability. Typically, Amazon Q will recognize your intention, which triggers it to offer suggestions. Another option is to send a code snippet with prompt instructions in an Amazon Q chat. For more information, see [Send code to Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/explain-update-code.html#send-code) in the *Amazon Q Developer User Guide*.

## Continuous comments
<a name="comments-troubleshooting"></a>

You might write a prompt using comments and only receive generic or repeated comment lines from Amazon Q.

Input:

```
// Kafka test
```

Result:

```
// Kafka test
// Kafka test
// Kafka test
// Kafka test
```

Typically, this issue is due to lack of context in the script or poor prompt instructions. We recommend that you use the standard format for comments given the language. In this example, the user changed the prompt to use `/* */ `for a comment block, and that change resulted in better performance from Amazon Q.

Input:

```
/*
 * Create a unit test to push a message to a Kafka topic
 */
```

Result:

In this result, the user accepted several suggestions sequentially.

```
/*
 * Create a unit test to push a message to a Kafka topic
 */
import org.junit.Test;
import java.util.Properties;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import static org.junit.Assert.assertEquals;
// create function for a Kafka test
public class KafkaTest {
    @Test
    public void testKafka() {
        // create Kafka producer
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        KafkaProducer<String, String> producer = new KafkaProducer<>(props);
        // create Kafka topic
        String topic = "test";
        // send message to Kafka topic
        producer.send(new ProducerRecord<>(topic, "key", "value"));
        // close Kafka producer
        producer.close();
        // assert that message was sent successfully
        assertEquals("value", KafkaTest.consumer.poll().value());
    }
}
```

## Incorrect in-line code generation
<a name="code-generation-troubleshooting"></a>

Occasionally, Amazon Q Developer in-line suggestions aren't useful or don't meet your prompt's objective. At times, in-line code suggestions might provide a generic function that's similar to a simple Hello World method.

When in-line code suggestions aren't helpful, try the following best practices:
+ Review the context of the script. Usually, the more context that you provide, the better results you get from Amazon Q.
+ If the context varies and/or is noisy, modularize your code. Group similar functions within the same script. Separate different classes and functions by their objective.
+ Write your class and function names tactically to help Amazon Q provide better recommendations.

In this example, the developer is writing a script from scratch which uploads files to Hadoop.

Input:

```
class  MyFunction{

    // create function to read data locally and upload to HDFS filesystem
```

Result:

```
class  MyFunction{

    // create function to read local data file path and upload to HDFS filesystem
    public void readAndUploadToHDFS(String inputPath, String outputPath) throws IOException {
        // read data from local file
        BufferedReader in = new BufferedReader(new FileReader(inputPath));

}
```

Although Amazon Q provided a recommendation, it didn't meet the developer's expectation. To improve performance, the developer imports libraries and changes the class name to represent Hadoop utilities.

Fix:

```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.FileReader;

// import applicable hadoop libraries for IO operations
import org.apache.hadoop.fs.Path;

class  HadoopUtilities{

    // create function to read local data file path and upload to HDFS filesystem
}
```

Result:

In this result, the developer accepted several suggestions sequentially.

```
class  HadoopUtilities{

    // create function to read local data file path and upload to HDFS filesystem
    public static void uploadToHDFS(String localFilePath, String hdfsFilePath) throws IOException {
        // create HDFS file path object
        Path hdfsPath = new Path(hdfsFilePath);
        // create local file path object
        Path localPath = new Path(localFilePath);
        // create hadoop file system object
        org.apache.hadoop.fs.FileSystem hdfs = org.apache.hadoop.fs.FileSystem.get(new org.apache.hadoop.conf.Configuration());
        // upload local file to HDFS
        hdfs.copyFromLocalFile(localPath, hdfsPath);
        // close HDFS file system
        hdfs.close();
        System.out.println("File uploaded successfully!");
}
```

In the same HadoopUtilities script, the developer adds a comment prompt to read an Amazon Simple Queue Service (Amazon SQS) topic.

Input:

```
// read message from SQS
```

Result:

```
// read message from SQS
    public static void readMessageFromSQS(String message) {
        System.out.println("Received message from SQS: " + message);
```

Rather that use Java methods to read an SQS message from Amazon SQS, Amazon Q suggests printing a string method. However, this suggestion doesn't satisfy the developer's original objective.

In this case, it's preferable to re-modularize the code. The script's focus is on Hadoop methods. Therefore, it might be a better approach to create a utility script that's specifically for SQS operations.

Creating a separate class for SQS utilities improves the in-line suggestion, which can be used in the HadoopUtilities script.

Input:

```
// import function for SQS
import com.amazonaws.services.sqs.AmazonSQS;
import java.util.ArrayList;
import java.util.List;

class SQSUtils {

    // instantiate SQS client
    private AmazonSQS sqsClient;

    // load SQS object
    public SQSUtils(AmazonSQS sqsClient) {
        this.sqsClient = sqsClient;
    }

    // poll message from Amazon SQS given queue name
}
```

Result:

```
// poll message from Amazon SQS given queue name
    public List<String> pollMessages(String queueName) {
        List<String> messages = new ArrayList<>();
        // poll messages from queue
        receiveMessageResult = sqsClient.receiveMessage(new ReceiveMessageRequest(queueName));
        for (Message message : receiveMessageResult.getMessages()) {
            messages.add(message.getBody());
        }
        return messages;
```

If the in-line suggestion is still not providing expected results, ask Amazon Q Developer in a chat session to generate code.

**Start Amazon Q chat about generating code**

User:

Generate a java function to read a message from an Amazon SQS queue

Amazon Q:

Here is an example Java function to read a message from an Amazon SQS queue:

```
import com.amazonaws.services.sqs.AmazonSQS;
import com.amazonaws.services.sqs.model.Message;
import com.amazonaws.services.sqs.model.ReceiveMessageRequest;
import com.amazonaws.services.sqs.model.ReceiveMessageResult;
public class SQSMessageReader {
    private AmazonSQS sqsClient;
    private String queueUrl;

    public SQSMessageReader(AmazonSQS sqsClient, String queueUrl) {
        this.sqsClient = sqsClient;
        this.queueUrl = queueUrl;
    }

    public String readMessage() {
        ReceiveMessageRequest receiveMessageRequest = new ReceiveMessageRequest(queueUrl)
                .withMaxNumberOfMessages(1)
                .withWaitTimeSeconds(10);

        ReceiveMessageResult receiveMessageResult = sqsClient.receiveMessage(receiveMessageRequest);

        if (receiveMessageResult.getMessages().size() > 0) {
            Message message = receiveMessageResult.getMessages().get(0);
            String messageBody = message.getBody();
            String receiptHandle = message.getReceiptHandle();

            // Process the message
            System.out.println("Received message: " + messageBody);

            // Delete the message from the queue
            sqsClient.deleteMessage(queueUrl, receiptHandle);

            return messageBody;
        } else {
            return null;
        }
    }
```

This code creates a SQSMessageReader class that takes an AmazonSQS client and a queue URL as constructor parameters. The readMessage() method uses the ReceiveMessageRequest to fetch up to 1 message from the queue, with a maximum wait time of 10 seconds.

If a message is received, the message body is printed and the message is deleted from the queue using the DeleteMessageRequest. The message body is then returned. If no message is received, null is returned.

**End** **Amazon Q chat about generating code**

## Inadequate results from chats
<a name="chat-results-troubleshooting"></a>

While developing code, developers can ask Amazon Q to generate common functions, provide recommendations, or explain code. Sometimes, given a prompt (such as a question or code snippet), Amazon Q might provide either general feedback or results that don't meet your expectations. In these scenarios, try the following:
+ Experiment with different prompts to improve the code generation results that you get from Amazon Q.
+ Follow the URLs that Amazon Q frequently provides in its responses to your prompts or questions.
+ Provide feedback to help improve future performance of Amazon Q.

For example, a developer is creating a Retrieval Augmented Generation (RAG) solution and they need to chunk their document given semantic relationships between sentences. The developer chats with Amazon Q as follows:

**Start** **Amazon Q** **chat about a RAG solution**

User:

For a RAG solution, generate code for semantic chunking

Amazon Q:

Certainly, here's an example of how you could implement semantic chunking for a Retrieval Augmented Generation (RAG) solution in Python using the LangChain library:

```
from langchain.text_splitter import CharacterTextSplitter, TokenTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Initialize the text splitter
text_splitter = TokenTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len
)
# Initialize the embeddings model
embeddings = HuggingFaceEmbeddings()

# Create the vector store
vectorstore = Chroma(
    embedding_function=embeddings.embed_documents,
    persist_directory="./chroma-data"
)

# Chunk the text using semantic similarity
def semantic_chunk(text):
    chunks = text_splitter.split_text(text)
    embeddings = embeddings.embed_documents(chunks)
    vectorstore.add_texts(chunks, embeddings)
    return chunks
```

In this example, we're using the TokenTextSplitter from LangChain to split the input text into chunks of 500 characters with an overlap of 50 characters. The HuggingFaceEmbeddings model is used to generate embeddings for each chunk, and the Chroma vector store is used to store the chunks and their embeddings.

The semantic\_chunk function takes in the input text, splits it into chunks using the text\_splitter, generates embeddings for each chunk using the embeddings model, and then adds the chunks and their embeddings to the vectorstore.

This approach allows you to split the input text into semantically meaningful chunks, which can be useful for a variety of tasks, such as question answering or summarization, in a RAG solution.

Please note that this is a basic example, and you may need to adjust the parameters (e.g., chunk\_size, chunk\_overlap) or the choice of text splitter and embeddings model based on your specific use case and data.

**End of Amazon Q** **chat about a RAG solution**

However, this approach only provides a basic way to chunk documents by using the sliding window technique. The developer wants an advanced way that relies on measuring embeddings. In these scenarios, the developer must add more specifics to the prompt given their objective. When the developer refers to the known AI21 text splitter function with LangChain, they receive an improved response as shown in the following chat.

**Start of Amazon Q** **chat about a RAG solution** **(with improved prompt)**

User:

The prompt above only relates to splitting regarding token size per chunk. I want to use AI21 Semantic text splitter. Generate a function using A121 semantic text splitting with langchain.

Amazon Q:

Okay, let's use the AI21 Semantic Text Splitter with LangChain to implement semantic chunking. Here's an example: [1]

```
from langchain.text_splitter import AI21SemanticTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Initialize the text splitter
text_splitter = AI21SemanticTextSplitter()

# Initialize the embeddings model
embeddings = HuggingFaceEmbeddings()

# Create the vector store
vectorstore = Chroma(
    embedding_function=embeddings.embed_documents,
    persist_directory="./chroma-data"
)

# Chunk the text using semantic similarity
def semantic_chunk(text):
    chunks = text_splitter.split_text(text)
    embeddings = embeddings.embed_documents(chunks)
    vectorstore.add_texts(chunks, embeddings)
    return chunks
```

In this example, we're using the AI21SemanticTextSplitter from LangChain to split the input text into semantically meaningful chunks. The HuggingFaceEmbeddings model is used to create embeddings for each chunk, and the Chroma vector store is used to store the chunks and their embeddings.

The semantic\_chunk function takes in the input text, splits it into chunks using the text\_splitter, creates embeddings for each chunk using the embeddings model, and then adds the chunks and their embeddings to the vectorstore.

This approach allows you to split the input text into semantically meaningful chunks, which can be useful for a variety of tasks, such as question answering or summarization, in a RAG solution.

Please note that you may need to adjust the parameters or the choice of embeddings model based on your specific use case and data.

Sources [1] Learn how to use text splitters in LangChain

[soosweb3.hashnode.dev > the-ultimate-langchain-series-text-splitters](https://blog.davideai.dev/the-ultimate-langchain-series-text-splitters)

**End of Amazon Q** **chat about a RAG solution** **(with improved prompt)**

Based on the chat results, the developer can use the function and navigate to the source of the information.

In general, advanced topics and questions require more specific context within the prompt when you chat with Amazon Q Developer. If you believe that the results from your chat aren't accurate, use the thumbs-down icon to provide feedback about the Amazon Q response. Amazon Q Developer continuously uses feedback to improve future releases. For interactions that produced positive results, it's useful to provide your feedback by using the thumbs-up icon.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
