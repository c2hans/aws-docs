---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/using-keyword-filters-for.html
---

# Using keyword filters for more accurate answers and customizing `"don’t know"` answers
<a name="using-keyword-filters-for"></a>

The keyword filter feature helps the guidance to be more accurate when answering questions with OpenSearch Service, and to admit more readily when it doesn’t know the answer.

## Keyword filters
<a name="keyword-filters"></a>

The keyword filter feature works by using [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html) to determine the part of speech that applies to each word you say to QnABot on AWS. By default, nouns (including proper nouns), verbs, and interjections are used as keywords. Any answer returned by QnABot on AWS must have questions that match these keywords, using the following (default) rule:
+ If there are one or two keywords, then all keywords must match.
+ If there are three or more keywords, then 75% of the keywords must match.

If you have selected a non-English language for your deployment, then it uses [Amazon Translate](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html) to translate these keywords back to the language your user is using for interaction. If QnABot on AWS can’t find any answers that match these keyword filter rules, then it admits that it doesn’t know the answer rather than guessing an answer that doesn’t match the keywords. The guidance logs every question that it can’t answer so you can see them in OpenSearch Dashboards.

## Custom `"Don’t Know"` answers
<a name="custom-dont-know-answers"></a>

When QnABot on AWS can’t find an answer, by default you’ll see or hear the response, ` "You stumped me! Sadly, I don’t know how to answer your question" `. You can customize this answer by creating a new item in the content designer, called the `no_hits` item:

1. From the content designer, choose **ADD** to create a new item:

   1. Enter ID: `CustomNoMatches`

   1. Enter question: `no_hits`

   1. Enter answer: `Terribly sorry, but I don’t know that one. Ask me another.`

1. Choose **CREATE** to save the item.

1. Use the web UI to ask: ` "What are Echo Buds?" `
