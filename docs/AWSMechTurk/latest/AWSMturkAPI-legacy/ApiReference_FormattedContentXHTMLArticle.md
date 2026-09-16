---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_FormattedContentXHTMLArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Formatted Content: XHTML
<a name="ApiReference_FormattedContentXHTMLArticle"></a>

**Topics**
+ [Using Formatted Content](#ApiReference_FormattedContentXHTMLArticle-using-formatted-content)
+ [Supported XHTML Tags](#ApiReference_FormattedContentXHTMLArticle-supported-xhtml-tags)
+ [How XHTML Formatted Content Is Validated](#ApiReference_FormattedContentXHTMLArticle-how-xhtml-formatted-content-is-validated)

 When you create a HIT or a Qualification test, you can include various kinds of content to be displayed to the Worker on the Amazon Mechanical Turk web site, such as text (titles, paragraphs, lists), media (pictures, audio, video) and browser applets (Java or Flash).

 You can also include blocks of formatted content. Formatted content lets you include XHTML tags directly in your instructions and your questions for detailed control over the appearance and layout of your data.

 You include a block of formatted content by specifying a `FormattedContent` element in the appropriate place in your [QuestionForm data structure](ApiReference_QuestionFormDataStructureArticle.md). You can specify any number of `FormattedContent` elements in content, and you can mix them with other kinds of content.

 The following example uses other content types (`Title`, `Text`) along with `FormattedContent` to include a table in a HIT:

```
<Text>
  This HIT asks you some questions about a game of Tic-Tac-Toe
  currently in progress.  Your answers will help decide the next move.
</Text>
<Title>The Current Board</Title>
<Text>
  The following table shows the board as it currently stands.
</Text>
<FormattedContent><![CDATA[
<table border="1">
  <tr>
    <td></td>
    <td align="center">1</td>
    <td align="center">2</td>
    <td align="center">3</td>
  </tr>
  <tr>
    <td align="right">A</td>
    <td align="center"><b>X</b></td>
    <td align="center">&nbsp;</td>
    <td align="center"><b>O</b></td>
  </tr>
  <tr>
    <td align="right">B</td>
    <td align="center">&nbsp;</td>
    <td align="center"><b>O</b></td>
    <td align="center">&nbsp;</td>
  </tr>
  <tr>
    <td align="right">C</td>
    <td align="center">&nbsp;</td>
    <td align="center">&nbsp;</td>
    <td align="center"><b>X</b></td>
  </tr>
  <tr>
    <td align="center" colspan="4">It is <b>X</b>'s turn.</td>
  </tr>
</table>
]]></FormattedContent>
```

 For more information about describing the contents of a HIT or Qualification test, see [the QuestionForm data structure](ApiReference_QuestionFormDataStructureArticle.md).

## Using Formatted Content
<a name="ApiReference_FormattedContentXHTMLArticle-using-formatted-content"></a>

 As you can see in the example above, formatted content is specified in an XML CDATA block, inside a `FormattedContent` element. The CDATA block contains the text and XHTML markup to display in the Worker's browser.

 Only a subset of the XHTML standard is supported. For a complete list of supported XHTML elements and attributes, see the table below. In particular, JavaScript, element IDs, `class` and `style` attributes, and `<div>` and `<span>` elements are not allowed.

 XML comments (`<!-- ... -->`) are not allowed in formatted content blocks.

 Every XHTML tag in the CDATA block must be closed before the end of the block. For example, if you start an XHTML paragraph with a `<p>` tag, you must end it with a `</p>` tag within the same `FormattedContent` block.

**Note**
 The tag closure requirement means you cannot open an XHTML tag in one `FormattedContent` block and close it in another. There is no way to "wrap" other kinds of question form content in XHTML. `FormattedContent` blocks must be self-contained.

 XHTML tags must be nested properly. When tags are used inside other tags, the inner-most tags must be closed before outer tags are closed. For example, to specify that some text should appear in bold italics, you would use the `<b>` and `<i>` tags as follows:

```
<b><i>This text appears bold italic.</i></b>
```

 But the following would not be valid, because the closing `</b>` tag appears before the closing `</i>` tag:

```
<b><i>These tags don't nest properly!</b></i>
```

 Finally, formatted content must meet other requirements to validate against the XHTML schema. For instance, tag names and attribute names must be all lowercase letters, and attribute values must be surrounded by quotes.

 For details on how Amazon Mechanical Turk validates XHTML formatted content blocks, see "How XHTML Formatted Content Is Validated," below.

## Supported XHTML Tags
<a name="ApiReference_FormattedContentXHTMLArticle-supported-xhtml-tags"></a>

 `FormattedContent` supports a limited subset of [the XHTML 1.0 ("transitional") standard](http://www.w3.org/TR/xhtml1/). The complete list of supported tags and attributes appears in the table below. Notable differences with the standard include:
+  JavaScript is not allowed. The `<script>` tag is not supported, and anchors (`<a>`) and images (`<img>`) cannot use `javascript:` targets in URLs.
+  CSS is not allowed. The `<style>` tag is not supported, and the `class` and `style` attributes are not supported. The `id` attribute is also not supported.
+  XML comments (`<!-- ... -->`) are not supported.
+  URL methods in anchor targets and image locations are limited to the following: `http:// https:// ftp:// news:// nntp:// mailto:// gopher:// telnet://`

 Other things to note with regards to supported tags and attributes:
+  In addition to the attributes listed, the `title` attribute is supported for all tags, and the `dir` and `lang` attributes are supported for all tags except `<br>`.
+  The `alt` attribute is required for `<area>` and `<img>` tags.
+  `<img>` tags also require a `src` attribute.
+  `<map>` tags require a `name` attribute.

 The following table lists the supported tags and attributes:

| Tag | Attributes |
| --- | --- |
|  a  |  accesskey charset coords href hreflang name rel rev shape tabindex target type  |
|  area  |  alt coords href nohref shape target  |
|  b  |    |
|  big  |    |
|  blockquote  |  cite  |
|  br  |    |
|  center  |    |
|  cite  |    |
|  code  |    |
|  col  |  align char charoff span valign width  |
|  colgroup  |  align char charoff span valign width  |
|  dd  |    |
|  del  |  cite datetime  |
|  dl  |    |
|  em  |    |
|  font  |  color face size  |
|  h1  |  align  |
|  h2  |  align  |
|  h3  |  align  |
|  h4  |  align  |
|  h5  |  align  |
|  h6  |  align  |
|  hr  |  align noshade size width  |
|  i  |  |
|  img  |  align alt border height hspace ismap longdesc src usemap vspace width  |
|  ins  |  cite datetime  |
|  li  |  type value  |
|  map  |  name  |
|  ol  |  compact start type  |
|  p  |  align  |
|  pre  |  width  |
|  q  |  cite  |
|  `small`  |  ``  |
|  strong  |     |
|  sub  |     |
|  sup  |     |
|  table  |  align bgcolor border cellpadding cellspacing frame rules summary width  |
|  tbody  |  align char charoff valign  |
|  td  |  abbr align axis bgcolor char charoff colspan headers height nowrap rowspan scope valign width  |
|  tfoot  |  align char charoff valign  |
|  th  |  abbr align axis bgcolor char charoff colspan headers height nowrap rowspan scope valign width  |
|  thead  |  align char charoff valign  |
|  tr  |  align bgcolor char charoff valign  |
|  u  |    |
|  ul  |  compact type  |

## How XHTML Formatted Content Is Validated
<a name="ApiReference_FormattedContentXHTMLArticle-how-xhtml-formatted-content-is-validated"></a>

 When you create a HIT or a Qualification test whose content uses `FormattedContent`, Amazon Mechanical Turk attempts to validate the formatted content blocks against a schema. If the formatted content does not validate against the schema, the operation call will fail and return an error.

 To validate the formatted content, Amazon Mechanical Turk takes the contents of the `FormattedContent` element (the text and markup inside the CDATA), then constructs an XML document with an appropriate XML header, `<FormattedContent>` as the root element, and the text and markup as the element's contents (without the CDATA). This document is then validated against a schema.

 For example, consider the following `FormattedContent` block:

```
  ...
  <FormattedContent><![CDATA[
    I absolutely <i>love</i> chocolate ice cream!
  ]]></FormattedContent>
  ...
```

 To validate this block, Amazon Mechanical Turk produces the following XML document:

```
<?xml version="1.0"?>
<FormattedContent xmlns="http://www.w3.org/1999/xhtml">
  I absolutely <i>love</i> chocolate ice cream!
</FormattedContent>
```

 The schema used for validation is called `FormattedContentXHTMLSubset.xsd`. For information on how to download this schema, see [WSDL and Schema Locations](ApiReference_WsdlLocationArticle.md).

 You do not need to specify the namespace of the XHTML tags in your formatted content. This is assumed automatically during validation.
