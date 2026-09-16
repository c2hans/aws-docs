---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ExternalQuestionArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# ExternalQuestion
<a name="ApiReference_ExternalQuestionArticle"></a>

**Topics**
+ [Description](#ApiReference_ExternalQuestionArticle-description)
+ [The ExternalQuestion Data Structure](#ApiReference_ExternalQuestionArticle-the-externalquestion-data-structure)
+ [Example](#ApiReference_ExternalQuestionArticle-example)
+ [The External Form](#ApiReference_ExternalQuestionArticle-the-external-form)
+ [Using Crowd HTML Elements](#ApiReference_ExternalQuestionArticle-crowd)
+ [The Answer Data](#ApiReference_ExternalQuestionArticle-the-answer-data)
+ [Guidelines For Using External Questions](#ApiReference_ExternalQuestionArticle-guidelines-for-using-external-questions)

## Description
<a name="ApiReference_ExternalQuestionArticle-description"></a>

Instead of providing a [QuestionForm data structure](ApiReference_QuestionFormDataStructureArticle.md) that tells Amazon Mechanical Turk how to display your questions and collect answers, you can host the questions on your own website using an "external" question.

A HIT with an external question displays a web page from your website in a frame in the Worker's web browser. Your web page displays a form for the Worker to fill out and submit. The Worker submits results using your form, and your form submits the results back to Amazon Mechanical Turk. Using your website to display the form gives your website control over how the question appears and how answers are collected.

To use an external question with a HIT, you provide an `ExternalQuestion` data structure as the value of the `Question` parameter when calling the `CreateHIT` operation. As with the `QuestionForm` data structure, an `ExternalQuestion` is a string value that consists of XML data. This data must conform to the `ExternalQuestion` schema. See [Data Structure Schema Locations](ApiReference_SchemaLocationArticle.md) for the location of this schema. For more information about using XML data as a parameter or return value, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

**Note**
 You can only use an external question as the question of a HIT. You cannot use an external question with a Qualification test.

## The ExternalQuestion Data Structure
<a name="ApiReference_ExternalQuestionArticle-the-externalquestion-data-structure"></a>

 The `ExternalQuestion` data structure has a root element of **ExternalQuestion**.

 The **ExternalQuestion** element contains the following elements:

| Name | Description | Required |
| --- | --- | --- |
|  `ExternalURL`  | The URL of your web form, to be displayed in a frame in the Worker's web browser. This URL must use the HTTPS protocol.<br />Type: URL<br />Default: None<br />Amazon Mechanical Turk appends the following parameters to this URL: `assignmentId`, `hitId`, `turkSubmitTo`, and `workerId`. For more information about these appended parameters, see the sections following this table.  | Yes |
|  `FrameHeight`  | The height of the frame, in pixels.<br />If you set the value to 0, your HIT will automatically resize to fit within the Worker's browser window.<br />Type: Integer<br />Default: None | Yes |

## Example
<a name="ApiReference_ExternalQuestionArticle-example"></a>

The following is an example of a complete `ExternalQuestion` data structure. Remember that to pass this structure in as the value of a parameter to an operation, XML characters must be escaped as character entities. For more information about escaping XML characters, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md). See [Data Structure Schema Locations](ApiReference_SchemaLocationArticle.md) for the location of this schema.

```
<?xml version="1.0" encoding="UTF-8"?>
<ExternalQuestion xmlns="{{[the ExternalQuestion schema URL]}}">
  <ExternalURL>https://tictactoe.amazon.com/gamesurvey.cgi?gameid=01523</ExternalURL>
  <FrameHeight>0</FrameHeight>
</ExternalQuestion>
```

## The External Form
<a name="ApiReference_ExternalQuestionArticle-the-external-form"></a>

When a Worker attempts to complete a HIT with an external question, the external website is loaded into a frame in the middle of the screen. The web page at that URL should display a form for the Worker to fill out, and all the information the Worker will need to complete the HIT.

### The Frame's URL and Parameters
<a name="ApiReference_ExternalQuestionArticle-the-external-form-the-frames-url-and-parameters"></a>

The URL used for the frame is the `ExternalURL` of the question with the following parameters appended: `assignmentId`, `hitId`, `turkSubmitTo`, and `workerId`. These parameters are appended CGI-style: The full URL has a question mark (`?`) before the first parameter, and an ampersand (`&`) between each parameter, with each parameter consisting of a name, an equal sign (`=`), and a value. Other parameters already present in this style in `ExternalURL` are preserved, so the final URL will only have one question mark, and all parameters will be separated by ampersands (`&`).

**Note**
 The URL you use for the `ExternalURL` must use the HTTPS protocol.

For example, consider an `ExternalURL` of:

```
https://tictactoe.amazon.com/gamesurvey.cgi?gameid=01523
```

 With this `ExternalURL`, the full URL used for the page in the frame could be as follows:

```
https://tictactoe.amazon.com/gamesurvey.cgi?gameid=01523
&assignmentId=123RVWYBAZW00EXAMPLE456RVWYBAZW00EXAMPLE
&hitId=123RVWYBAZW00EXAMPLE
&turkSubmitTo=https://www.mturk.com/
&workerId=AZ3456EXAMPLE
```

### Preview Mode
<a name="ApiReference_ExternalQuestionArticle-the-external-form-preview-mode"></a>

 Your external question will be displayed when a Worker previews the HIT on the Amazon Mechanical Turk website, before the Worker has clicked the "Accept HIT" button. When the HIT is being previewed, the URL will have a special value for the `assignmentId`: `ASSIGNMENT_ID_NOT_AVAILABLE`.

When a Worker previews a HIT, your web page should show her everything she will need to do to complete the HIT, so she can decide whether or not to accept it. The easiest way to do this is to simply display the form as it would appear when the HIT is accepted. However, you may want to take precautions to prevent a Worker from accidentally filling out or submitting your form prior to accepting the HIT.

 You can use JavaScript or server-side logic to check the `assignmentId` parameter, and change the display of the form if the HIT is being previewed (`assignmentId=ASSIGNMENT_ID_NOT_AVAILABLE`).

 If a Worker submits your form before accepting the HIT, and your form attempts to post the data back to Amazon Mechanical Turk, Amazon Mechanical Turk will display an error message to the Worker, and the results will not be accepted.

### The Form Action
<a name="ApiReference_ExternalQuestionArticle-the-external-form-the-form-action"></a>

The form on the external website must post the result data back to Amazon Mechanical Turk using the following URL:

```
https://www.mturk.com/mturk/externalSubmit
```

 Or, if you are using the Amazon Mechanical Turk sandbox, you should post the result data back to Mechanical Turk using the following sandbox URL:

```
https://workersandbox.mturk.com/mturk/externalSubmit
```

 The form must include the `assignmentId` field that was appended to the URL used to access your form. It should be submitted along with the other form fields submitted by your form, with a name of `assignmentId` and the same value as was passed to the form. Be sure to spell the field name as it appears here, with the same letters uppercase and lowercase.

**Note**
The field names `assignmentId`, `hitId`, `turkSubmitTo`, and `workerId` are reserved for special purposes. Your form only needs to submit the `assignmentId` field. Any data submitted with a field name of "`hitId`" will be ignored, and will not appear in the results data for the HIT.

The form must submit data to that URL using the "POST" method. The data the form submits should be name-value pairs in the CGI-style:
+ Each field appears as the name, an equal sign, and the value. For example: `favoriteColor=blue`
+ Data that appears in the posted URL is preceded by a question mark (`?`), and is delimited by ampersands (`&`). For example:

  ```
  https://www.mturk.com/mturk/externalSubmit?favoriteColor=blue&favoriteNumber=7&...
  ```
+ Data that appears in the HTTP message body (using the "POST" method) has one data pair per line. For example:

  ```
  favoriteColor=blue
  favoriteNumber=7
  ...
  ```

 The easiest way to post the data in the CGI-style is to use an HTML form on the web page, with the `externalSubmit` URL as the "action," and "POST" as the "method."

## Using Crowd HTML Elements
<a name="ApiReference_ExternalQuestionArticle-crowd"></a>

The External Question supports [Crowd HTML Elements](ApiReference_HTMLCustomElementsArticle.md). Based on HTML web components, they encapsulate HTML, CSS, and JavaScript functionality behind a single HTML element. For example, the `<crowd-form>` element sets up your form for you, setting the correct submission endpoint and inserting a submit button at the end. Other elements provide question widgets or design elements you can customize to create more tailored HIT structures.

### Requirements
<a name="ApiReference_ExternalQuestionArticle-crowd-requirements"></a>

There are three requirements for using Crowd HTML elements:
+ You must place the elements between the `<crowd-form>` opening and closing elements. As noted above, these also invisibly set up a `<form>` element and place a "submit" button at the bottom.

+ Place the Crowd HTML Elements loader script before the opening `<crowd-form>` element.

+ Store the HTML file in an S3 bucket, make the file publicly accessible, and reference it in the `<ExternalURL>` element of your XML .

Try this sample sentiment analysis form.

**Example**

```
<!DOCTYPE html>
<html>
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
```

Between the `<classification-target>` opening and closing tags, you can put any HTML that could be rendered and classified. For example you could use an audio clip or a video clip.

For more details, read the [Crowd HTML Elements](ApiReference_HTMLCustomElementsArticle.md) article or view the [Element Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html) to see the different elements that are available.

## The Answer Data
<a name="ApiReference_ExternalQuestionArticle-the-answer-data"></a>

When the Worker submits your form, the form sends the field data to Amazon Mechanical Turk using the `externalSubmit` URL, and Amazon Mechanical Turk records the field data as the results of the Assignment.

When you retrieve the results using `ListAssignmentsForHIT`, the field data submitted by your form will appear in the `Answer` of the [Assignment](ApiReference_AssignmentDataStructureArticle.md) as if each field were a free-text answer. The `QuestionIdentifier` element of the answer will be the name of the field, and the `FreeText` element will contain the value.

See the [QuestionFormAnswers data format](ApiReference_QuestionFormAnswersDataStructureArticle.md) for more information about the format of answer data.

## Guidelines For Using External Questions
<a name="ApiReference_ExternalQuestionArticle-guidelines-for-using-external-questions"></a>

External questions give your application a great deal of power over how Workers submit results for your HITs. To ensure you get good results for your HITs, you should make sure your web server and web pages can provide your Workers with a quality experience.

Because external questions depend on your web server for rendering the question form, both while Workers are previewing HITs and while Workers are completing HITs, your server will need to be engineered for high availability. The Amazon Mechanical Turk website gets heavy traffic, so your web server will need to be able to respond quickly and correctly when receiving many requests in a short period of time.

**Tip**
 [Amazon S3](http://aws.amazon.com/s3) offers high availability of data, accessible via public HTTPS URLs. You can host your external questions as web pages in Amazon S3, and not have to run your own server. When you use an S3-hosted layout, you need to add a `ContentType` header and set the ACL to public read, as shown in the following Python SDK [PutObject](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object) call:

```
s3_client.put_object(
   ACL='public-read',
   Body={{HTML layout}},
   Bucket={{S3 bucket name}},
   Key={{Object name}},
   ContentType="text/html"
)
```

 Your website can do many things inside the frame, but eventually it must cause the Worker's browser to load the "externalSubmit" URL in the frame with the results in POST data. The easiest way to do this is with an HTML form whose fields contain the HIT results, with a submit button that the Worker will click. If an external HIT prevents the Worker from submitting results back to Amazon Mechanical Turk using the "externalSubmit" mechanism, the Worker may not be able to claim rewards or continue doing work without restarting their session. Amazon Mechanical Turk reserves the right to remove any external HITs that are not functioning properly.

**Note**
 Your HIT will be rendered inside an IFRAME that has certain limitations. The IFRAME operates in HTML5 "sandbox" mode that has extra restrictions on the content that can appear in the frame. This limits your ability to execute certain code and to use technologies such as Adobe Flash. To ensure your HITs work as expected, we recommend you test them first in the [Requester Sandbox](https://requester.mturk.com/developer/sandbox).

Finally, please remember that external questions must meet the Amazon Mechanical Turk Participation Agreement, and Amazon Mechanical Turk's standards for appropriate content. Specifically, the Participation Agreement expressly prohibits the use of Amazon Mechanical Turk for advertising or solicitation. If your website typically displays advertising to visitors, please make sure those advertisements do not appear in your external questions. Amazon Mechanical Turk reserves the right to remove HITs with inappropriate content.
