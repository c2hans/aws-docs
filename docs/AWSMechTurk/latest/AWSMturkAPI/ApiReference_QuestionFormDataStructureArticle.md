---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QuestionFormDataStructureArticle.html
---

# QuestionForm
<a name="ApiReference_QuestionFormDataStructureArticle"></a>

**Topics**
+ [Description](#ApiReference_QuestionFormDataStructureArticle-description)
+ [QuestionForm Structure](#ApiReference_QuestionFormDataStructureArticle-questionform-structure)
+ [Content Structure](#ApiReference_QuestionFormDataStructureArticle-content-structure)
+ [Answer Specification](#ApiReference_QuestionFormDataStructureArticle-answer-specification)
+ [Example](#ApiReference_QuestionFormDataStructureArticle-example)

## Description
<a name="ApiReference_QuestionFormDataStructureArticle-description"></a>

 The `QuestionForm` data format describes one or more *questions* for a HIT, or for a Qualification test. It contains instructions and data Workers use to answer the questions, and a set of one or more form fields, which are rendered as a web form for a Worker to fill out and submit.

 A `QuestionForm` is a string value that consists of XML data. This XML data must conform to the `QuestionForm` schema. All elements in a `QuestionForm` belong to a namespace whose name is identical to the URL of the `QuestionForm` schema document. See [Schema Locations](ApiReference_SchemaLocationArticle.md) for the location of this schema.

**Tip**
 For information about creating HITs that use your own web site in a frame instead of questions, see [the ExternalQuestion data structure](ApiReference_ExternalQuestionArticle.md).

 The `QuestionForm` data structure is used as a parameter value for the following operations:
+  `CreateHIT and CreateHITWithHITType`
+  `CreateQualificationType`
+  `UpdateQualificationType`

 For more information about using XML data as a parameter or return value, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

## QuestionForm Structure
<a name="ApiReference_QuestionFormDataStructureArticle-questionform-structure"></a>

 The top-most element of the `QuestionForm` data structure is a `QuestionForm` element. This element contains optional `Overview` elements and one or more `Question` elements. There can be any number of these two element types listed in any order. The following example structure has an `Overview` element and a `Question` element followed by a second `Overview` element and `Question` element—all within the same `QuestionForm`.

```
<QuestionForm xmlns="{{[the QuestionForm schema URL]}}">
  <Overview>
    {{[...]}}
  </Overview>
  <Question>
    {{[...]}}
  </Question>
  <Overview>
    {{[...]}}
  </Overview>
  <Question>
    {{[...]}}
  </Question>
  {{[...]}}
</QuestionForm>
```

 The `Overview` element describes instructions and information, and presents them separately from the set of questions. It can contain any kind of informational content, as described below. If omitted, no overview text is displayed above the questions.

 Each `Question` element can contain the elements described in the following table. See also the example below the table.

| Name | Description | Required |
| --- | --- | --- |
|  `QuestionIdentifier`  |  An identifier for the question. This identifier is used to associate the Worker's answers with the question in the answer data. <br />Type: String <br />Default: None | Yes |
|  `DisplayName`  |  A name for the question, displayed as a prominent heading. <br />Type: String<br />Default: None | No |
|  `IsRequired`  |  Specifies whether the Worker must provide an answer for this question to successfully submit the form. <br />Type: Boolean<br />Default: false<br />Valid Values: true \| false | No |
|  `QuestionContent`  |  The instructions and data specific to this question, such as the text of the question. It can contain any kind of informational content, as described in the *Content Structure* section below. <br />Type: Content structure<br />Default: None | Yes |
|  `AnswerSpecification`  |  A structure that describes the field type and possible values for the answer to this question, as described in the *Answer Specification* section below. This element controls how the form field is rendered and specifies which values are valid answers for this question. <br />Type: An answer specification structure<br />Default: None<br /> Valid Values: `FreeTextAnswer` \| `SelectionAnswer` \| `FileUploadAnswer`  | Yes |

 For example:

```
  <Question>
    <QuestionIdentifier>my_question_id</QuestionIdentifier>
    <DisplayName>My Question</DisplayName>
    <IsRequired>true</IsRequired>
    <QuestionContent>
      {{[...]}}
    </QuestionContent>
    <AnswerSpecification>
      {{[...]}}
    </AnswerSpecification>
  </Question>
```

## Content Structure
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure"></a>

 The `Overview` elements and the `QuestionContent` elements of a `QuestionForm` can contain different types of information. For example, you might include a paragraph of text and an image in your HIT's overview.

 Each kind of information is defined by a corresponding element. These elements can appear in any number, in any order. The content elements are rendered in the order in which they occur in the containing element.

 Following are the allowed information types:
+ Title
+ Text
+ List
+ Binary
+ Application (Deprecated)
+ EmbeddedBinary
+ FormattedContent

 Each of these types are described in detail in the following subsections. A full example showing the use of the elements and information types is at the end of the section.

### Title
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure-title"></a>

 A `Title` element specifies a string to be rendered as a title or heading.

```
<Title>The Next Move</Title>
```

### Text
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure-text"></a>

 A `Text` element specifies a block of text to be rendered as a paragraph. Only plain text is allowed. HTML is not allowed. If HTML characters (such as angle brackets) are included in the data, they appear verbatim in the web output.

```
<Text>What is the best next move for "X" in this game of Tic-Tac-Toe?</Text>
```

### List
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure-list"></a>

 A `List` element displays a bulleted list of items. Items are specified using one or more `ListItem` elements inside the `List`. The `ListItem` element is a string.

```
<List>
  <ListItem>It must be a valid move.</ListItem>
  <ListItem>"X" cannot resign.</ListItem>
</List>
```

### Binary
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure-binary"></a>

 A `Binary` element specifies non-textual data of some kind, such as an image, audio, or video. The elements listed in the following table are required and must be entered in the order shown here.

| Name | Description | Required |
| --- | --- | --- |
|  `MimeType`  | Specifies the type of the data.<br />Type: `MimeType` element<br />Default: None<br />Child Elements:+   A required string that specifies the type of the data. The possible values are **image**, **audio**, or **video**.  <br />+   An optional string that specifies the format of the item, such as **gif**   | Yes |
|  `DataURL`  |  The data itself specified with a `DataURL` element that contains a valid HTTP URL. <br />Type: `DataURL` element<br />Default: None | Yes |
|  `AltText`  |  The text that should appear if the data cannot be rendered in the browser. <br />Type: String<br />Default: None | Yes |

```
<Binary>
  <MimeType>
    <Type>image</Type>
    <SubType>gif</SubType>
  </MimeType>
  <DataURL>http://tictactoe.amazon.com/game/01523/board.gif</DataURL>
  <AltText>The game board, with "X" to move.</AltText>
</Binary>
```

### Application (Deprecated)
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure-application"></a>

**Important**
Beginning Tuesday, December 12th 2017 the QuestionForm data structure will **no longer support the `Application` element.** Instead, we recommend using the [HTMLQuestion](ApiReference_HTMLQuestionArticle.md) or [ExternalQuestion](ApiReference_ExternalQuestionArticle.md) data structures for including interactive content for Workers.

 An `Application` element specifies an embedded application. It contains either a `JavaApplet` element or a `Flash` element.

 You can specify zero or more parameters to pass to your Java applet or Flash application when it is opened in the web page. For a HIT, in addition to the parameters you specify, Amazon Mechanical Turk includes two parameters specific to the HIT: `hitId` and `assignmentId`. The `hitId` parameter is equal to the ID of the HIT. The `assignmentId` parameter is equal to the ID of the assignment if the Worker has accepted the HIT, or equal to `ASSIGNMENT_ID_NOT_AVAILABLE` if the Worker is only previewing the HIT.

 The `JavaApplet` element includes the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `AppletPath`  | The URL path to the directory that contains Java classes for the applet.<br />Type: URL<br />Default: None | Yes |
|  `AppletFilename`  | The name of the class file that contains the applet code, which is located in the path specified by `AppletPath`.<br />Type: String<br />Default: None | Yes |
|  `Width`  | The width of the bounding box for the applet.<br />Type: String<br />Default: None | Yes |
|  `Height`  | The height of the bounding box for the applet.<br />Type: String<br />Default: None | Yes |
|  `ApplicationParameter`  | The parameters for the applet.<br />Type: `ApplicationParameter` <br />Default: None<br />Child Elements:+   A required string that specifies the name of the parameter  <br />+   A required string that specifies the value of the parameter   | No |

 The `Flash` element includes the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `FlashMovieURL`  | The URL of the Flash movie file.<br />Type: URL<br />Default: None | Yes |
|  `Width`  | The width of the bounding box for the Flash movie.<br />Type: String<br />Default: None | Yes |
|  `Height`  | The height of the bounding box for the Flash movie.<br />Type: String<br />Default: None | Yes |
|  `ApplicationParameter`  |  The parameters for the Flash movie. <br />Type: `ApplicationParameter` <br />Default: None<br />Child Elements:+   A required string that specifies the name of the parameter  <br />+   A required string that specifies the value of the parameter   | No |

```
<Application>
  <JavaApplet>
    <AppletPath>http://tictactoe.amazon.com/applets/</AppletPath>
    <AppletFilename>GameViewer.class</AppletFilename>
    <Width>400</Width>
    <Height>300</Height>
    <ApplicationParameter>
      <Name>game_id<Name>
      <Value>01523</Value>
    </ApplicationParameter>
  </JavaApplet>
</Application>
```

### EmbeddedBinary
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure-embeddedbinary"></a>

 An `EmbeddedBinary` element specifies an external object of non-textual data of some kind, such as an image, audio or video, that displays in your browser. The elements listed in the following table are required and must be entered in the order shown here.

| Name | Description | Required |
| --- | --- | --- |
|  `EmbeddedMimeType`  | Specifies the type of the data.<br />Type: `EmbeddedMimeType` element<br />Default: None<br />Child Elements:+   A required string that specifies the type of the data. The possible values are **image**, **audio**, or **video**. <br />+  An optional string that specifies the format of the item, such as **gif**  | Yes |
|  `DataURL`  |  The data itself specified by a `DataURL` element that contains a valid HTTP URL <br />Type: `DataURL` element<br />Default: None | Yes |
|  `AltText`  |  The text that should appear if the data cannot be rendered in the browser. <br />Type: String<br />Default: None | Yes |
|  `Width`  |  The width of the bounding box for the object. <br />Type: String<br />Default: None | Yes |
|  `Height`  |  The height of the bounding box for the object. <br />Type: String<br />Default: None | Yes |
|  `ApplicationParameter`  | The parameters for the `EmbeddedBinary` object. <br />Type: `ApplicationParameter` <br />Default: None<br />Child elements:+   A required string that specifies the name of the parameter <br />+   A required string that specifies the value of the parameter  | No |

```
<EmbeddedBinary>
  <EmbeddedMimeType>
    <Type>image</Type>
    <SubType>gif</SubType>
  </EmbeddedMimeType>
  <DataURL>http://tictactoe.amazon.com/game/01523/board.gif</DataURL>
  <AltText>The game board, with "X" to move.</AltText>
  <Width>400</Width>
  <Height>300</Height>
  <ApplicationParameter>
    <Name>game_id<Name>
    <Value>01523</Value>
  </ApplicationParameter>
</EmbeddedBinary>
```

### FormattedContent
<a name="ApiReference_QuestionFormDataStructureArticle-content-structure-formattedcontent"></a>

 For finer control over the display of your HIT information, you can specify a `FormattedContent` element. Formatted content is a block of text with formatting information specified using XHTML tags. For example, you can use XHTML tags to specify that certain words appear in a boldface font or to include a table in your HIT information.

 Only a limited subset of XHTML is supported. For more information on the creating and validating XHTML formatted content, see [Formatted Content: XHTML](ApiReference_FormattedContentXHTMLArticle.md).

 The value of the `FormattedContent` element must be specified as an XML CDATA block. CDATA tells the web service that the XHTML elements are not part of the `QuestionForm` data schema. For example, the following describes a paragraph of formatted text:

```
<FormattedContent><![CDATA[
  <p>This is a paragraph with <b>bold text</b>,
  <i>italic text</i>, and <b><i>bold italic text</i></b>.</p>
]]></FormattedContent>
```

## Answer Specification
<a name="ApiReference_QuestionFormDataStructureArticle-answer-specification"></a>

 The `AnswerSpecification` element describes the format and possible values for answers to a question. It contains a `FreeTextAnswer` element, which describes a text field; a `SelectionAnswer` element, which describes a multiple choice field; or a `FileUploadAnswer`, which prompts the Worker to upload a file as the answer to the question.

### FreeTextAnswer
<a name="ApiReference_QuestionFormDataStructureArticle-answer-specification-freetextanswer"></a>

 A `FreeTextAnswer` element describes a text field and constraints on its possible values. It includes the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `Constraints`  |  Describes the constraints on the allowed values for the text field. This element is described in the next table. <br />Type: `Constraints` element<br />Default: None | No |
|  `DefaultText`  |  Specifies default text. This value appears in the form when it is rendered, and is accepted as the answer if the Worker does not change it. <br />Type: String<br />Default: An empty value | No |
|  `NumberOfLinesSuggestion`  |  Specifies how tall the form field should be, if possible. The field might be rendered as a text box with this many lines, depending on the device the Worker is using to see the form. <br />Type: Integer<br />Default: 1 | No |

**Note**
 A Qualification test that is to be graded automatically using an answer key cannot have any free-text questions. An answer key can only match multiple-choice questions and cannot match free-text fields.

 The optional `Constraints` element describes constraints on the allowed values for the text field. If no constraints are specified, any value is accepted for the field.

 The `Constraints` element includes the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `IsNumeric`  | Specifies that the value entered must be numeric.<br />Type: empty element<br />Default: None<br />Attributes:+  An optional integer that specifies the minimum value allowed <br />+  An optional integer that specifies the maximum value allowed  | No |
|  `Length`  | Specifies the length range of the answer.<br />Type: empty element<br />Default: None<br />Attributes:+   An optional non-negative integer that specifies the minimum number of characters  <br />+   An optional positive integer that specifies the maximum number of characters   | No |
|  `AnswerFormatRegex`  |  Specifies that JavaScript validates the answer string against a given pattern.   A limitation of this approach is that Workers who have disabled JavaScript on their browsers cannot validate their answers. Although this is uncommon, you might want to caution your Workers.  <br />Type: empty element<br />Default: None<br />Attributes:+  A required string that specifies the regular expression that JavaScript uses to validate against the Workers' entered values <br />+  An optional string that allows you to edit the content of errors displayed to the Worker on the Worker web site if the regex validation fails. If this attribute is not specified, the error displayed is "Invalid input supplied."  <br />+  An optional string with the value `i` which specifies that case is ignored when matching characters   | No |

 The `Constraints` element can contain multiple `AnswerFormatRegex` elements. All `AnswerFormatRegex` constraints must be satisfied before the Worker can submit the HIT.

 The following examples demonstrate how to use the `FreeTextAnswer` element.

 If you want a 3-digit positive integer between 100 and 999, use the following:

```
<FreeTextAnswer>
  <Constraints>
    <IsNumeric minValue="100" maxValue="999"/>
    <Length minLength="3" maxLength="3"/>
  </Constraints>
</FreeTextAnswer>
```

 If you want a 3-digit number that includes decimals, use the following:

```
<FreeTextAnswer>
  <Constraints>
     <IsNumeric/>
     <Length minLength="3" maxLength="3"/>
  </Constraints>
</FreeTextAnswer>
```

 If you want to ensure that there is some text, use the following example. The **minLength** attribute includes whitespaces in the character count.

```
<FreeTextAnswer>
  <Constraints>
    <Length minLength="2" />
    <AnswerFormatRegex regex="\S" errorText="The content cannot be blank."/>
  </Constraints>
</FreeTextAnswer>
```

 If you specify the **minLength** attribute, it is the same as if the ` IsRequired ` element is `true`. If you want to allow an *optional* string that must be at least two characters, use the following:

```
<FreeTextAnswer>
  <Constraints>
    <AnswerFormatRegex regex="(^$|\S{2,})"
     errorText="You must enter at least two characters."/>
  </Constraints>
</FreeTextAnswer>
```

 To request a US phone number in the format 1-nnn-nnn-nnnn, where "1-" is optional, use the following:

```
<FreeTextAnswer>
  <Constraints>
    <AnswerFormatRegex
     regex="^(1[- ]?)?(\([2-9]\d{2}\)\s*|[2-9]\d{2}-?)[2-9]\d{2}-?\d{4}$)"
     errorText="You must enter a US phone number in the format
     1-555-555-1234 or 555-555-1234."/>
  </Constraints>
</FreeTextAnswer>
```

 If you want an answer that contains a date formatted as yyyy-mm-dd, use the following:

```
<FreeTextAnswer>
  <Constraints>
    <AnswerFormatRegex regex="^[12][0-9]{3}-[01]?\d-[0-3]?\d$"
     errorText="You must enter a date with the format yyyy-mm-dd."/>
  </Constraints>
</FreeTextAnswer>
```

 If you want an answer that contains "regex" and variations including RegEx, REGex, and RegExes, use the following:

```
<FreeTextAnswer>
  <Constraints>
    <AnswerFormatRegex regex="regex" flags="i"
     errorText="You must enter 'regex'."/>
  </Constraints>
</FreeTextAnswer>
```

### SelectionAnswer
<a name="ApiReference_QuestionFormDataStructureArticle-answer-specification-selectionanswer"></a>

 A `SelectionAnswer` describes a multiple-choice question. Depending on the element defined, the Worker might be able to select zero, one, or multiple items from a set list as the answer to the question.

 A `SelectionAnswer` element includes the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `MinSelectionCount`  |  Specifies the minimum number of selections allowed for a valid answer. This value can range from 0 to the number of selections. <br />Type: non-negative Integer<br />Default: 1 | No |
|  `MaxSelectionCount`  |  Specifies the maximum number of selections allowed for a valid answer. This value can range from 1 to the number of selections. <br />Type: positive Integer<br />Default: 1 | No |
|  `StyleSuggestion`  |  Specifies what style of multiple-choice form field to use when displaying the question to the Worker. The field might not use the suggested style, depending on the device the Worker is using to see the form. <br />Type: String<br />Default: None<br />Valid Values:+   Can be used if `MaxSelectionCount` is **1**, because it restricts the user to selecting either zero or one item from the list  <br />+   Allows multiple selections, but can be restricted by using the `MaxSelectionCount` element  <br />+   Allows multiple selections, but can be restricted by using the `MaxSelectionCount` element  <br />+   Can be used if `MaxSelectionCount` is **1**, because it restricts the user to selecting either zero or one item from the list  <br />+   Allows multiple selections, but can be restricted by using the `MaxSelectionCount` element  <br />+   Allows multiple selections, but can be restricted by using the `MaxSelectionCount` element   | No |
|  `Selections`  | Specifies the answer selections.<br />Type: `Selections` structure<br />Default: None<br />Child elements:+   Specifies an answer selection. This element is described fully in the next table.  <br />+   An optional text field to display below the selection list that allows the Worker to enter an alternate answer that does not appear in the list of selections. The contents of this element are similar to `FreeTextAnswer`.    A Qualification test that you want to grade automatically using an answer key cannot have an `OtherSelection` field for a multiple choice question. An answer key can only match multiple-choice questions and cannot match free-text fields.    | Yes |

 The `Selections` element lists the selection options available. It contains one or more `Selection` elements, one for each possible answer in the set. The `Selection` element includes the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `SelectionIdentifier`  |  A unique alphanumeric string that is in the answer data if this selection is chosen. <br />Type: String<br />Default: None | Yes |
|  One of the following elements:  |  | Yes |
|  `Text`  | Contains the content of the selected item.<br />Type: String<br />Default: None |
|  `FormattedContent`  |  A block of text formatted using XHTML tags that contains the content of the selected item. For more information about this format, see [Formatted Content: XHTML](ApiReference_FormattedContentXHTMLArticle.md). <br />Type: String<br />Default: None |
|  `Binary`  | Contains the content of the selected item.<br />Type: `Binary`<br />Default: None |

 The following example shows a `SelectionAnswer` element that specifies a question with four radiobuttons.

```
<SelectionAnswer>
  <StyleSuggestion>radiobutton</StyleSuggestion>
  <Selections>
    <Selection>
      <SelectionIdentifier>C1</SelectionIdentifier>
      <Text>C1 (northeast)</Text>
    </Selection>
    <Selection>
      <SelectionIdentifier>C2</SelectionIdentifier>
      <Text>C2 (east)</Text>
    </Selection>
    <Selection>
      <SelectionIdentifier>A3</SelectionIdentifier>
      <Text>A3 (southwest)</Text>
    </Selection>
    <Selection>
      <SelectionIdentifier>C3</SelectionIdentifier>
      <Text>C3 (southeast)</Text>
    </Selection>
  </Selections>
</SelectionAnswer>
```

### FileUploadAnswer (Deprecated)
<a name="ApiReference_QuestionFormDataStructureArticle-answer-specification-fileuploadanswer"></a>

**Important**
Beginning Tuesday, December 12th 2017 the Answer Specification structure will **no longer support the `FileUploadAnswer` element** to be used for the QuestionForm data structure. Instead, we recommend that Requesters who want to create HITs asking Workers to upload files use [Amazon S3](http://aws.amazon.com/s3).

 A `FileUploadAnswer` prompts the Worker to upload a file as the answer to the question. When the Worker uploads the file, Amazon Mechanical Turk stores the file separately from the answer data. Once the HIT is submitted, your application can call the `GetFileUploadURL` operation to get a temporary URL it can use to download the file.

 The `FileUploadAnswer` specification contains two required elements, a `MinFileSizeInBytes` and a `MaxFileSizeInBytes`, that specify the minimum and maximum allowed file sizes respectively. If the Worker uploads a file whose size in bytes is outside of this range, the answer is rejected, and the Worker must upload a different file to complete the HIT. You can specify a maximum size up to 2000000000 (2 billion) bytes.

**Note**
 A `FileUploadAnswer` element can only be used with HITs. It cannot be used with Qualification tests.

 The following example demonstrates a `FileUploadAnswer` element that specifies a file with a minimum of 1000 bytes and a maximum of 3000000 bytes.

```
<FileUploadAnswer>
  <MaxFileSizeInBytes>3000000</MaxFileSizeInBytes>
  <MinFileSizeInBytes>1000</MinFileSizeInBytes>
</FileUploadAnswer>
```

## Example
<a name="ApiReference_QuestionFormDataStructureArticle-example"></a>

 The following is an example of a complete `QuestionForm` data structure. Remember that to pass this structure in as a value of a parameter to an operation, XML characters must be escaped as character entities. (See [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md) for more information.)

```
<QuestionForm xmlns="{{[the QuestionForm schema URL]}}">
  <Overview>
    <Title>Game 01523, "X" to play</Title>
    <Text>
      You are helping to decide the next move in a game of Tic-Tac-Toe.  The board looks like this:
    </Text>
    <Binary>
      <MimeType>
        <Type>image</Type>
        <SubType>gif</SubType>
      </MimeType>
      <DataURL>http://tictactoe.amazon.com/game/01523/board.gif</DataURL>
      <AltText>The game board, with "X" to move.</AltText>
    </Binary>
    <Text>
      Player "X" has the next move.
    </Text>
  </Overview>
  <Question>
    <QuestionIdentifier>nextmove</QuestionIdentifier>
    <DisplayName>The Next Move</DisplayName>
    <IsRequired>true</IsRequired>
    <QuestionContent>
      <Text>
        What are the coordinates of the best move for player "X" in this game?
      </Text>
    </QuestionContent>
    <AnswerSpecification>
      <FreeTextAnswer>
        <Constraints>
          <Length minLength="2" maxLength="2" />
        </Constraints>
        <DefaultText>C1</DefaultText>
      </FreeTextAnswer>
    </AnswerSpecification>
  </Question>
  <Question>
    <QuestionIdentifier>likelytowin</QuestionIdentifier>
    <DisplayName>The Next Move</DisplayName>
    <IsRequired>true</IsRequired>
    <QuestionContent>
      <Text>
        How likely is it that player "X" will win this game?
      </Text>
    </QuestionContent>
    <AnswerSpecification>
      <SelectionAnswer>
        <StyleSuggestion>radiobutton</StyleSuggestion>
        <Selections>
          <Selection>
            <SelectionIdentifier>notlikely</SelectionIdentifier>
            <Text>Not likely</Text>
          </Selection>
          <Selection>
            <SelectionIdentifier>unsure</SelectionIdentifier>
            <Text>It could go either way</Text>
          </Selection>
          <Selection>
            <SelectionIdentifier>likely</SelectionIdentifier>
            <Text>Likely</Text>
          </Selection>
        </Selections>
      </SelectionAnswer>
    </AnswerSpecification>
  </Question>
</QuestionForm>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
