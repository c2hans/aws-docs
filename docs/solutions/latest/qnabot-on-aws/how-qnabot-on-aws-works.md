---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/how-qnabot-on-aws-works.html
---

# How QnABot on AWS works
<a name="how-qnabot-on-aws-works"></a>

This guidance uses the same technology as Alexa. Amazon Lex provides the tools to tackle challenging problems such as speech recognition and language understanding through an easy-to-use fully managed service. Amazon Lex integrates with AWS Lambda to run your backend business logic for data retrieval and updates. After you build your bot, you can deploy it to chat platforms, mobile clients, and IoT devices. You can also use reports to track bot metrics. This guidance provides a scalable, secure, and easy-to-use way to build, publish, and monitor your bots.

Intelligent contact centers leverage conversational UX engines like Amazon Lex in order to provide proactive service to customers. Amazon Lex uses a deep learning engine that combines ASR and NLU to manage the customer experience. This enables it to be natural and adaptable to customer needs.

Chatbots are the starting point for many organizations. Amazon Lex comes with both voice and text. Amazon Lex has many application integrations for popular messaging platforms such as Slack and Facebook.

For Interactive Voice Response systems you can utilize the Text to speech capabilities of Amazon Polly to relay the response back in the voice of your choice.

To help fulfill many self-service requests, you can integrate Amazon Lex with your data or applications to retrieve information or use Amazon Kendra to search for the most accurate answers from your unstructured data sets.

The following figure illustrates a reference architecture for how QnABot on AWS integrates with external components.

 **Reference architecture for QnABot on AWS integrations with external components**

![ref architecture integrations](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/ref-architecture-integrations.png)

The following figure illustrates how Amazon Lex and Amazon OpenSearch Service help power the QnABot on AWS guidance.

 **How Amazon Lex and Amazon OpenSearch Service help power the QnABot on AWS guidance.**

![arch data flow](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/arch-data-flow.png)

Asking QnABot on AWS questions initiates the following processes:

1. The question gets processed and transcribed by Amazon Lex using NLU and Natural Language Processing (NLP) engines.

1. The guidance initially trains the NLP engine to match a wide variety of possible questions and statements so that the Amazon Lex chatbot can accept almost any question a user asks. The Amazon Lex interaction model is set up with the following:
   +  **intents** - An intent represents an action that fulfills a user’s spoken request. Intents can optionally have arguments called *slots*. The guidance uses *slots* to capture user input and fulfill the intent via a Lambda function.
   +  **sample utterances** - A set of likely spoken phrases mapped to the intents. This should include as many representative phrases as possible. The sample utterances specify the words and phrases users can say to invoke your intents. The guidance updates the **sample utterances** with the various questions to train the chatbot to understand different end user’s input.

1. This question is then sent to Amazon OpenSearch Service. The guidance attempts to match an end user’s request to the list of questions and answers stored in Amazon OpenSearch Service.
   + The QnABot on AWS uses full-text search to find the most relevant ranked document from the searchable index. Relevancy ranking is based on a few properties:
     +  **count** - How many search terms appear in a document.
     +  **frequency** - How often the specified keywords occur in a given document.
     +  **importance** - How rare or new the specified keywords are and how closely the keywords occur together in a phrase.
   + The closer the alignment between a question associated with an item and a question asked by the user, the greater the probability that the guidance will choose that item as the most relevant answer. Noise words such as articles and prepositions in sentence construction have lower weighting than unique keywords.
   + The keyword filter feature helps the guidance to be more accurate when answering questions, and to admit more readily when it doesn’t know the answer. The keyword filter feature works by using Amazon Comprehend to determine the part of speech that applies to each word you say to QnABot on AWS. By default, nouns (including proper nouns), verbs, and interjections are used as keywords. Any answer returned by QnABot on AWS must have questions that match these keywords, using the following (default) rule:
     + If there are one or two keywords, then all keywords must match.
     + If there are three or more keywords, then 75% of the keywords must match.
     + If QnABot on AWS can’t find any answers that match these keyword filter rules, then it will admit that it doesn’t know the answer rather than guessing an answer that doesn’t match the keywords. QnABot on AWS logs every question that it can’t answer so you can see them in the included Kibana Dashboard.
     + The Bot fulfillment Lambda function generates an Amazon OpenSearch Service query containing the transcribed question. The query attempts to find the best match from all the questions and answers you’ve previously provided, filtering items to apply the keyword filters and using Amazon OpenSearch Service relevance scoring to rank the results. Scoring is based on 1) matching the words in the end user’s question against the unique set of words used in the stored questions (`quniqueterms`), 2) matching the phrasing of the user’s question to the text of stored questions (nested field `questions.q`), and 3) matching the topic value assigned to the previous answer (if any) to increase the overall relevance score when the topic value (field `t`) matches. The following example code shows an Amazon OpenSearch query:

       ```
       "query":{
           "bool": {
               "filter": {
                   "match": {
                       "quniqueterms": {
                           "query": "<LIST_OF_IDENTIFIED_KEYWORDS>",
                           "minimum_should_match":
                                 "<ES_MINIMUM_SHOULD_MATCH SETTING>",
                           "zero_terms_query": "all"
                       }
                   }
               },
               "should": [
                   {
                       "match": {
                           "quniqueterms": {
                               "query": "<USER QUESTION>",
                               "boost": 2
                           }
                       }
                   },
                   {
                       "nested": {
                           "score_mode": "max",
                           "boost": "<ES_PHRASE_BOOST SETTING>",
                           "path": "questions",
                           "query": {
                               "match_phrase": {
                                   "questions.q": "<USER QUESTION>"
                               }
                           }
                       }
                   },
                   {
                       "match": {
                           "t": "<PREVIOUS_TOPIC>"
                       }
                   }
               ]
           }
       }
       ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
