---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/documents.html
---

# AWS Documents
<a name="documents"></a>

The AWS Toolkit for Visual Studio Code supports the AWS Serverless Application Model `JSON Schema` for `AWS SAM templates`, enhancing the template authoring experience by enabling definitions, autocompletion, and validation directly in VS Code. AWS Documents supports all AWS SAM and CloudFormation resources. For additional details see the following resources:
+ For specific information about JSON Schema, see the [JSON Schema](https://json-schema.org/) JSON-Schema.org website.
+ For additional information about AWS SAM templates, see the [AWS SAM template anatomy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html) topic in the *AWS Serverless Application Model* Developer Guide.
+ For additional information about AWS resources and property types, see the [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) topic in the *CloudFormation* User Guide.
+ For detailed information about the AWS SAM schema utilized by the AWS Toolkit, see the [AWS Serverless Application Model](https://github.com/aws/serverless-application-model/blob/main/samtranslator/schema/schema.json) schema in the AWS GitHub repository.

## Getting Started with AWS Documents
<a name="documents-getstarted"></a>

To get started working with AWS Documents in VS Code, install the AWS Toolkit for Visual Studio Code extension from your IDE or the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode), and open any AWS SAM template.

## Viewing documentation, autocompletion, and validation in VS Code
<a name="documents-autocomplete"></a>

Viewing documentation, autocompletion, and validation are features included with the AWS Toolkit. See the image below for an example of what these features look like in VS Code.
+ To view documentation from your open AWS SAM template, hover your pointer over a line-entry in the document.
+ For autocompletion, start typing in your AWS SAM template to activate a pop-up with suggestions based on your input.
+ Your AWS SAM template is automatically scanned for validation and errors are highlighted by a light bulb icon that you can select for additional suggestions.

See the image below for an example of what these features look like in VS Code.

![RestApiId property details for AWS::Serverless::Api resource in AWS SAM template.](http://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/filetypes2024.png)
