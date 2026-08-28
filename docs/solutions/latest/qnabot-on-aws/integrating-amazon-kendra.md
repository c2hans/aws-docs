---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/integrating-amazon-kendra.html
---

# Integrating Amazon Kendra
<a name="integrating-amazon-kendra"></a>

**Amazon Kendra end of new-customer availability**
Amazon Kendra will no longer be open to new customers starting on July 30, 2026. For QnABot deployments using Kendra as a fallback data source, we suggest Amazon Bedrock Knowledge Bases as an alternative. [Amazon Kendra availability change](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

 [Amazon Kendra](https://aws.amazon.com/kendra/) is an intelligent search service powered by machine learning. There are two ways to take advantage of Amazon Kendra’s NLP model to enhance the guidance’s ability to understand human questions:

1. Use Amazon Kendra’s FAQ queries to match users' questions to the answers in the guidance’s knowledge base. Amazon Kendra’s machine learning models can handle many variations in how users phrase their questions, and this can reduce the amount of tuning needed for the guidance to find the right answer from your knowledge base.

1. Use Amazon Kendra’s document index as a fallback source of answers when a question/answer is not found in the guidance’s knowledge base.

For more information, see [Amazon Kendra Pricing](https://aws.amazon.com/kendra/pricing/) and [Getting started](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html) in the *Amazon Kendra Developer Guide* to create your Amazon Kendra index\_.\_

## Using Amazon Kendra FAQ for question matching
<a name="using-kendra-faq-for-question-matching"></a>

Use the following procedure to configure the guidance to use your Amazon Kendra index to answer questions from the data populated in the content designer:

1. Set the **KendraFaqIndexId** CloudFormation parameter to the ID of the Amazon Kendra index to use. Find the index ID in the Amazon Kendra console.

1. Replicate all items from the content designer to the Amazon Kendra index:

   1. Select the menu (⋮) from the top right in the content designer.

   1. Choose **SYNC KENDRA FAQ** and wait for it to complete - it might take a few minutes.

The guidance now uses Amazon Kendra FAQ queries to find matches to end users' questions. Use the **ALT\_SEARCH\_KENDRA\_FAQ\_CONFIDENCE\_SCORE** setting to adjust the confidence threshold for Amazon Kendra FAQ answers used by QnABot on AWS.

If Amazon Kendra FAQ cannot find an answer that meets the confidence threshold, the guidance reverts by default to using an Amazon OpenSearch Service query. The combination of Amazon Kendra FAQ and Amazon OpenSearch Service gives you the best of both worlds.

**Note**
When adding your **Amazon KendraFaqIndexId** in CloudFormation, also add the index ID in **AltSearchAmazon KendraIndexes**.

## Using Amazon Kendra search as a fallback source of answers
<a name="using-amazon-kendra-search-as-a-fallback-source-of-answers"></a>

You can add one or more data sources to your Amazon Kendra index, and configure the guidance to query your index any time it gets a question that it doesn’t know how to answer.
+ Set the **AltSearchAmazon KendraIndexes** CloudFormation parameter to specify one or more Amazon Kendra indexes to use for fallback searches.

The value of **AltSearchAmazon KendraIndexes** parameter should be specified as a string containing index IDs separated by comma, for example:

 `857710ab-example-do-not-copy`
+ Or -

 `857710ab-example1-do-not-copy,857710ab-example2-do-not-copy`

QnABot on AWS also supports Amazon Kendra index authentication token pass through.
+ Set the **AltSearchAmazon KendraIndexes** CloudFormation parameter to specify one or more Amazon Kendra indexes to use for fallback searches. You must [control user access to documents with tokens](https://docs.aws.amazon.com/kendra/latest/dg/create-index-access-control.html) using OpenID. For more information, see the [Amazon Kendra Fallback Function](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/kendra_fallback) section in the GitHub repository.
+ Set the **AltSearchAmazon KendraIndexAuth** CloudFormation parameter to `TRUE`. This enables QnABot to send an OpenID Token to Amazon Kendra index(es) to limit Amazon Kendra results to which the user is entitled.
+ Input the **IDENTITY\_PROVIDER\_JWKS\_URLS** QnABot content designer settings parameter. Find your token key signing URL from the Cognito user pool of QnABot or `Lex-Web-Ui`.
**Note**
When configuring your Amazon Kendra index with user access control, Amazon Kendra only allows you to specify one signing key URL from one Cognito user pool. Having multiple Cognito pools, including `Lex-Web-Ui`, requires you to set up multiple Amazon Kendra indexes.

## Amazon Kendra redirect
<a name="amazon-kendra-redirect"></a>

QnABot on AWS supports multiple mechanisms for dynamic interaction flows. For example:
+ Using Lambda hooks in a given Item ID to perform additional actions, such as creating a ticket, resetting a password, and saving data to a data store.
+ Using an Amazon Kendra index as a fallback mechanism to look for answers to user’s questions.

There are various options to process Amazon Kendra queries. One option is to create a custom Lambda hook and map it to an Item ID. The Lambda hook then includes the business logic to use an Amazon Kendra index and process the query.

The Amazon Kendra redirect feature provides a much simpler option. You can include an Amazon Kendra query within an Item ID, and QnABot will do the rest to process the Amazon Kendra request and respond back with the results.

## Configuring an Item ID with Amazon Kendra redirect
<a name="configuring-an-item-id-with-amazon-kendra-redirect"></a>

You can configure an Item ID with Amazon Kendra Redirect UI.

 **Amazon Kendra redirect configuration**

![image26](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image26.png)

1. Create a QnABot question as you would normally do by providing an Item ID and questions and utterances.

1. Expand the **Advanced** option.

1.  **Amazon Kendra Redirect: Query Text** accepts a QueryText to search for (for example `what is q and a bot`) and retrieve the answer from the Amazon Kendra fallback index specified in the CloudFormation stack parameters. Amazon Kendra searches your index for text content, question, and answer (FAQ) content. You can also use Handlebars to substitute values using session attributes or slots to support dynamic queries.

1.  **Amazon Kendra Redirect: Confidence** score threshold provides a relative ranking that indicates how confident Amazon Kendra is that the response matches the query. This is an optional field having one of the values of: `LOW`, `MEDIUM`, `HIGH`, `VERY HIGH`. If no value is provided, the value for the **ALT\_KENDRA\_FALLBACK\_CONFIDENCE\_THRESHOLD** setting is used.

1.  **Amazon Kendra query arguments** is an optional field that allows filtered searches based on document attributes, for example, `"AttributeFilter": {"EqualsTo": {"Key": "City", "Value": {"StringValue": "Seattle"}}}`. You can also use Handlebars to substitute values using session attributes or slots to support dynamic queries.

For more information on using Amazon Kendra query arguments, see the [Amazon Kendra Query API](https://docs.aws.amazon.com/kendra/latest/dg/API_Query.html) in the *Amazon Kendra\_\_API Reference*.

**Note**
Answer fields are ignored when `Amazon KendraRedirect` query is used.
Use this feature for use cases where you have Item IDs that directly need to interact with an Amazon Kendra index as configured in the CloudFormation stack parameters.
When applying Amazon Kendra query arguments, check if the document fields are searchable. **Searchable** determines whether the field is used in the search. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) in the \_Amazon Kendra*\_Developer Guide*.

## Web page indexer
<a name="web-page-indexer"></a>

This guidance can answer questions based on the content of web pages.

1. In the CloudFormation stack, set the **Amazon KendraWebPageIndexId** parameter to `Existing Amazon Kendra Index ID`. Add the same index ID for the **AltSearchAmazon KendraIndexes** parameter.

1. From the content designer, select the tools menu (☰), and then choose **Settings.**

1. Modify the following settings:

   1.  **ENABLE\_WEB\_INDEXER:** true

   1. \*KENDRA\_INDEXER\_URLS: \* link:https://aws.amazon.com/lex/faqs/

   1.  **KENDRA\_INDEXER\_SCHEDULER:**https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html\#RateExpressions*   *

1. From the content designer, select the tools menu ( **☰** ), and then choose **Amazon Kendra Web Crawler**.

   1. Choose **START INDEXING**.

   1. Wait for indexing to complete. It can take several minutes.

1. Open the web UI, and ask ` "What is Lex?" `. QnABot on AWS provides an answer with a link to the Amazon Lex FAQ page.

For more information on web page indexing, see the [README.md](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/docs/kendra_crawler_guide) file in the GitHub repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for QnABot on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
