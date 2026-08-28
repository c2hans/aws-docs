---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_FormattedContentXHTMLArticle.html
---

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

 The schema used for validation is called `FormattedContentXHTMLSubset.xsd`. For information on how to download this schema, see [Data Structure Schema Locations](ApiReference_SchemaLocationArticle.md).

 You do not need to specify the namespace of the XHTML tags in your formatted content. This is assumed automatically during validation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
