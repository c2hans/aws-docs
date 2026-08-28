---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HTMLQuestionArticle.html
---

# HTMLQuestion
<a name="ApiReference_HTMLQuestionArticle"></a>

**Topics**
+ [Description](#ApiReference_HTMLQuestionArticle-description)
+ [The HTMLQuestion Data Structure](#ApiReference_HTMLQuestionArticle-the-HTMLQuestion-data-structure)
+ [Example](#ApiReference_HTMLQuestionArticle-example)
+ [Using Crowd HTML Elements](#ApiReference_HTMLQuestionArticle-crowd)
+ [Preview Mode](#ApiReference_HTMLQuestionArticle-the-external-form-preview-mode)
+ [The Form Action](#ApiReference_HTMLQuestionArticle-the-external-form-the-form-action)
+ [The Answer Data](#ApiReference_HTMLQuestionArticle-the-answer-data)
+ [Guidelines For Using HTML Questions](#ApiReference_HTMLQuestionArticle-guidelines-for-using-external-questions)

## Description
<a name="ApiReference_HTMLQuestionArticle-description"></a>

 The `HTMLQuestion` data structure defines one or more questions for a HIT using HTML. The `HTMLQuestion` data structure is similar to both the `QuestionForm` and `ExternalQuestion` data structures.

The `QuestionForm` data structure defines, using a special XML language, how Amazon Mechanical Turk displays HIT questions and collects the answers. The `ExternalQuestion` data structure defines, using HTML, questions you host on your own "external" website. If you want to define your questions using HTML forms without having to host a website, you can use the `HTMLQuestion` data structure.

A `HTMLQuestion` HIT is like a cross between a `QuestionForm` HIT and an `ExternalQuestion` HIT, for instance:
+ Like a `QuestionForm` HIT, you do not need to run a website or run any other infrastructure to have your HIT display on Mechanical Turk. You define your question when you call CreateHIT and then collect worker answers later, after they have been submitted.
+  Like an `ExternalQuestion` HIT, you can define your HIT in HTML. Your HTML code must contain a form for the Worker to fill out and submit, which is displayed in a frame in the Worker's web browser. The Worker submits results using your form, and your form submits the results back to Amazon Mechanical Turk. Worker answers are processed by Mechanical Turk in the same way as `ExternalQuestion` HITs. If you choose, you can collect or process the results before submitting to Mechanical Turk.

The worker interaction and presentation options available for `HTMLQuestion` are similar to `ExternalQuestion`. HTMLQuestions differ from ExternalQuestions primarily in how they are created.

As with the other question data structures, an `HTMLQuestion` is a string value that consists of XML data. This data must conform to the `HTMLQuestion` schema. See [Data Structure Schema Locations](ApiReference_SchemaLocationArticle.md) for the location of this schema. For more information about using XML data as a parameter or return value, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

**Note**
You can only use an `HTMLQuestion` as the question of a HIT. You cannot use an `HTMLQuestion` with a Qualification test.

The `HTMLQuestion` data structure is used as a parameter value for the following operation:
+  `CreateHIT`

The `HTMLQuestion` data structure is a value in a [HIT](ApiReference_HITDataStructureArticle.md) data structure.

All elements in an `HTMLQuestion` belong to a namespace whose name is identical to the URL of the `HTMLQuestion` schema document for the version of the API you are using.

## The HTMLQuestion Data Structure
<a name="ApiReference_HTMLQuestionArticle-the-HTMLQuestion-data-structure"></a>

 The `HTMLQuestion` data structure has a root element of `HTMLQuestion`.

 The `HTMLQuestion` element contains the following elements:

| Name | Description | Required |
| --- | --- | --- |
|  `HTMLContent`  | The HTML code of your web form, to be displayed in a frame in the Worker's web browser. The HTML must validate against the HTML5 specification. HTML5 is backwards-compatible with a variety of recent HTML document specifications. For more information, see [http://www.w3.org/TR/html5-diff/](http://www.w3.org/TR/html5-diff/). For help in ensuring that your HTML validates, see [http://validator.w3.org](http://validator.w3.org).<br />Type: String<br />Default: None<br />Amazon Mechanical Turk appends the following parameters to this URL: `assignmentId`, `hitId`, `turkSubmitTo`, and `workerId`. For more information about these appended parameters, see the sections following this table. | Yes |
|  `FrameHeight`  | The height of the frame, in pixels.<br />If you set the value to 0, your HIT will automatically resize to fit within the Worker's browser window.<br />Type: Integer<br />Default: None | Yes |

## Example
<a name="ApiReference_HTMLQuestionArticle-example"></a>

The following is an example of a complete `HTMLQuestion` data structure. Remember that to pass this structure in as the value of a parameter to an operation, XML characters must be escaped as character entities. For more information, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

```
<HTMLQuestion xmlns="[the HTMLQuestion schema URL]">
  <HTMLContent><![CDATA[
<!DOCTYPE html>
<html>
 <head>
  <meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>
  <script type='text/javascript' src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js'></script>
 </head>
 <body>
  <form name='mturk_form' method='post' id='mturk_form' action='https://www.mturk.com/mturk/externalSubmit'>
  <input type='hidden' value='' name='assignmentId' id='assignmentId'/>
  <h1>What's up?</h1>
  <p><textarea name='comment' cols='80' rows='3'></textarea></p>
  <p><input type='submit' id='submitButton' value='Submit' /></p></form>
  <script language='Javascript'>turkSetAssignmentID();</script>
 </body>
</html>
]]>
  </HTMLContent>
  <FrameHeight>0</FrameHeight>
</HTMLQuestion>
```

## Using Crowd HTML Elements
<a name="ApiReference_HTMLQuestionArticle-crowd"></a>

The HTML Question supports [Crowd HTML Elements](ApiReference_HTMLCustomElementsArticle.md). Based on HTML web components, they encapsulate HTML, CSS, and JavaScript functionality behind a single HTML element. For example, the `<crowd-form>` element sets up your form for you, setting the correct submission endpoint and inserting a submit button at the end. Other elements provide question widgets or design elements you can customize to create more tailored HIT structures.

Try this sample sentiment analysis form.

**Example**

```
<HTMLQuestion xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd">
  <HTMLContent><![CDATA[
    <!DOCTYPE html>
      <body>
        <script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
        <crowd-form>
          <crowd-classifier
            name="sentiment"
            categories="['Positive', 'Negative', 'Neutral', 'N/A']"
            header="What sentiment does this text convey?"
          >
            <classification-target>
            Everything is wonderful.
            </classification-target>

            <full-instructions header="Sentiment Analysis Instructions">
            <p><strong>Positive</strong>
              sentiment include: joy, excitement, delight</p>
            <p><strong>Negative</strong> sentiment include:
              anger, sarcasm, anxiety</p>
            <p><strong>Neutral</strong>: neither positive or
              negative, such as stating a fact</p>
            <p><strong>N/A</strong>: when the text cannot be
              understood</p>
            <p>When the sentiment is mixed, such as both joy and sadness,
              use your judgment to choose the stronger emotion.</p>
            </full-instructions>

            <short-instructions>
             Choose the primary sentiment that is expressed by the text.
            </short-instructions>
          </crowd-classifier>
        </crowd-form>
      </body>
    </html>
  ]]></HTMLContent>
  <FrameHeight>0</FrameHeight>
</HTMLQuestion>
```

Between the `<classification-target>` opening and closing tags, you can put any HTML that could be rendered and classified. For example you could use an audio clip or a video clip.

For more details, read the [Crowd HTML Elements](ApiReference_HTMLCustomElementsArticle.md) article or view the [Element Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html) to see the different elements that are available.

## Preview Mode
<a name="ApiReference_HTMLQuestionArticle-the-external-form-preview-mode"></a>

The question defined by `HTMLQuestion` displays when a Worker previews the HIT on the Amazon Mechanical Turk website, before the Worker clicks the **Accept HIT** button. When the HIT is being previewed, the URL has a special value for the `assignmentId`: `ASSIGNMENT_ID_NOT_AVAILABLE`. This is the same mechanism used for `ExternalQuestion` HITs.

When a Worker previews a HIT, your HTML should show the Worker everything they will need to do to complete the HIT, so they can decide whether or not to accept it. The easiest way to do this is to simply display the form as it would appear when the HIT is accepted. However, you may want to take precautions to prevent a Worker from accidentally filling out or submitting your form prior to accepting the HIT.

You can use JavaScript to check the `assignmentId` parameter, and change the display of the form if the HIT is being previewed (`assignmentId=ASSIGNMENT_ID_NOT_AVAILABLE`).

## The Form Action
<a name="ApiReference_HTMLQuestionArticle-the-external-form-the-form-action"></a>

For information about form actions for `HTMLQuestion`, see " The Form Action" in [ExternalQuestion](ApiReference_ExternalQuestionArticle.md).

## The Answer Data
<a name="ApiReference_HTMLQuestionArticle-the-answer-data"></a>

For information about answer data for `HTMLQuestion`, see " The Answer Data" in [ExternalQuestion](ApiReference_ExternalQuestionArticle.md).

## Guidelines For Using HTML Questions
<a name="ApiReference_HTMLQuestionArticle-guidelines-for-using-external-questions"></a>

**Tip**
Your HTML code can do many things inside the browser frame, but eventually it must cause the Worker's browser to load the "externalSubmit" URL in the frame with the results in POST data. The easiest way to do this is with an HTML form whose fields contain the HIT results, with a submit button that the Worker clicks. If a `HTMLQuestion` HIT prevents the Worker from submitting results back to Amazon Mechanical Turk using the "externalSubmit" mechanism, the Worker may not be able to claim rewards or continue doing work without restarting their session. Amazon Mechanical Turk reserves the right to remove any `HTMLQuestion` HITs that are not functioning properly.

**Note**
Your HIT will be rendered inside an IFRAME that has certain limitations. The IFRAME operates in HTML5 “sandbox” mode that has extra restrictions on the content that can appear in the frame. This limits your ability to execute certain code and to use technologies such as Adobe Flash. To ensure your HITs work as expected, we recommend you test them first in the [Requester Sandbox](https://requester.mturk.com/developer/sandbox).

**Tip**
All `HTMLQuestion` HITs are served from the same domain, regardless of requester. Bear this in mind if you choose to set cookies from JavaScript in your HTML.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
