---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HTMLCustomElementsArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# Crowd HTML Elements
<a name="ApiReference_HTMLCustomElementsArticle"></a>

**Topics**
+ [Description](#ApiReference_HTMLCustomElementsArticle-description)
+ [Use Cases](#ApiReference_HTMLCustomElementsArticle-usecases)
+ [Examples](#ApiReference_HTMLCustomElementsArticle-examples)
+ [Element Reference](#ApiReference_HTMLCustomElementsArticle-elementref)
+ [Related Documents](#ApiReference_HTMLCustomElementsArticle-seealso)

## Description
<a name="ApiReference_HTMLCustomElementsArticle-description"></a>

**Crowd HTML Elements** extend the capabilities of the [ExternalQuestion](ApiReference_ExternalQuestionArticle.md) and [HTMLQuestion](ApiReference_HTMLQuestionArticle.md). They are web components that provide a number of task widgets and design elements that can be tailored to the question being asked.

## Use Cases
<a name="ApiReference_HTMLCustomElementsArticle-usecases"></a>

**Crowd HTML Elements** are web components, a web standard that abstracts HTML markup, CSS, and JavaScript functionality into an HTML tag or set of tags. If you'd like to see how that works, try the `<crowd-bounding-box>` example below. The element provides a bounding box widget which can be customized with different instructions, labels, and headers.

Other types of questions that can be customized include: semantic segmentation, image classification, text classification, utterance collection, and more.

## Examples
<a name="ApiReference_HTMLCustomElementsArticle-examples"></a>

To quickly try one of the examples below, open a text editor on your local machine, copy an example from this page, paste it into the text editor, and then save the file with whatever name you want and a `.html` extension. Open the file in a browser and the example should work. You can try customizing it further or adding other **Crowd HTML Elements** by exploring the [element reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html).

### Crowd HTML Essential Elements
<a name="ApiReference_HTMLCustomElementsArticle-examples-skel"></a>

Every use of **Crowd HTML Elements** requires two things:
+  The **Crowd HTML Elements** loader, which is a `<script>` element that should be placed before your form.

  `<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>`
+ Opening and closing `<crowd-form>` tags. Put your form's content between the tags. The benefit to these is that they set up the specifications for your form and the "submit" button. You write less code and need to remember fewer specific things.

### Crowd HTML Bounding Box
<a name="ApiReference_HTMLCustomElementsArticle-examples-BoundingBox"></a>

Try this bounding box example. Copy it, paste it, and run it in a browser as instructed above.

**Example**

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-bounding-box
    name="annotatedResult"
    labels="['Basketball player', 'Referee']"
    src="https://s3.amazonaws.com/cv-demo-images/basketball-outdoor.jpg"
    header="Draw boxes around each basketball player and referee in this image"
  >
    <full-instructions header="Bounding Box Instructions" >
      <p>Use the bounding box tool to draw boxes around the requested target of interest:</p>
      <ol>
        <li>Draw a rectangle using your mouse over each instance of the target.</li>
        <li>Make sure the box does not cut into the target, leave a 2 - 3 pixel margin</li>
        <li>
          When targets are overlapping, draw a box around each object,
          include all contiguous parts of the target in the box.
          Do not include parts that are completely overlapped by another object.
        </li>
        <li>
          Do not include parts of the target that cannot be seen,
          even though you think you can interpolate the whole shape of the target.
        </li>
        <li>Avoid shadows, they're not considered as a part of the target.</li>
        <li>If the target goes off the screen, label up to the edge of the image.</li>
      </ol>
    </full-instructions>

    <short-instructions>
      Draw boxes around each basketball player and referee in this image.
    </short-instructions>
  </crowd-bounding-box>
</crowd-form>
```

Pay attention to the attributes and regions of the `<crowd-bounding-box>` element. It requires the `header`, `labels`, `name`, and `src` attributes. It also requires the `<full-instructions>` and `<short-instructions>` regions, though what is put in them is up to you.

The sample will also display the form output when you press the "submit" button, so you can see the format of the output you will receive.

### Crowd HTML Sentiment Analysis
<a name="ApiReference_HTMLCustomElementsArticle-examples-sentiment"></a>

Try this sentiment analysis example. Copy it, paste it, and run it in a browser as instructed above.

**Example**

```
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
        <p><strong>Positive</strong> sentiments include: joy, excitement, delight</p>
        <p><strong>Negative</strong> sentiments include: anger, sarcasm, anxiety</p>
        <p><strong>Neutral</strong>: neither positive or negative, such as stating a fact</p>
        <p><strong>N/A</strong>: when the text cannot be understood</p>
        <p>When the sentiment is mixed, such as both joy and sadness, use your judgment to choose the stronger emotion.</p>
      </full-instructions>

      <short-instructions>
       Choose the primary sentiment that is expressed by the text.
      </short-instructions>
    </crowd-classifier>
</crowd-form>
```

This shares some characteristics with other elements, like the bounding box above. For example, they both require a name, a header, and instructions. One thing that's notably different is the `<classification-target>` region. That has simple text in it, but it can contain just about any HTML: a video clip, an audio clip, an animation, anything that can be represented in a browser and simply classified.

## Element Reference
<a name="ApiReference_HTMLCustomElementsArticle-elementref"></a>

**[The Custom HTML Element Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html)** provides a list of all supported custom elements, their requirements, attributes, and sample outputs (where appropriate).

## Related Documents
<a name="ApiReference_HTMLCustomElementsArticle-seealso"></a>
+ [HTMLQuestion](ApiReference_HTMLQuestionArticle.md)
+ [ExternalQuestion](ApiReference_ExternalQuestionArticle.md)
+ [Element Reference](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-ui-template-reference.html)
