---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/introduction.html
---

# Image classification solutions on AWS
<a name="introduction"></a>

*Matthew Chasse, Wale Akinfaderin, Mason Cahill, and Tayo Olajide, Amazon Web Services*

*Image classification* is a central task in computer vision, a subfield of machine learning (ML) and artificial intelligence (AI). Image classification algorithms analyze the pixels of an image and output labels for the entire image. For example, the following image might have the following labels: `person`, `dog`, or `outdoors`.

![Woman hiking outdoors with a dog.](https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/images/guide-img/3c71b76a-1e6e-4c69-b783-1676c6b7fb2d/images/bd475407-bd36-44cf-87ad-e79f65206875.png)

Image classification does not localize the objects in an image or create bounding boxes (as is done in object detection). Example applications of image classification include sorting images into digital albums and processing car images for inventory at an automobile dealership.

There are multiple AWS services and approaches that you can use to perform image classification on AWS. The goal of this guide is to help you find efficient solutions for image classification tasks. This guide discusses the following approaches:
+ Using [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)
+ Using [Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html)
+ Using [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
+ Using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
+ Creating and managing a custom training job in Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS)

This guide discusses the capabilities of each AWS service and how to determine which approach is best suited to your image classification task. In this guide, image classification solutions are organized around three traits:
+ **Model specification and training** – Determining the appropriate model architecture and training approach
+ **Deployment infrastructure type** – Determining the type of infrastructure the inference endpoint will use
+ **Operations automation and workflow** – Determining how you will maintain and update the solution

For the Amazon Rekognition service, model specification and training options are predetermined by the service; therefore, any desired model or training options beyond those offered must be created with custom code. This guide discusses the process of testing to determine if Amazon Rekognition or Amazon Rekognition Custom Labels is a good solution for your use case. Although there is a prebuilt image classification container in Amazon SageMaker AI, it is not sufficient for many production image-classification tasks. SageMaker AI also provides deep learning containers that permit customization and fine-tuning of pretrained models.

This guide presents an overall strategy for devising an image classification solution on AWS. It provides best practices for each portion of the strategy, providing advice about the available services and their capabilities.

## Objectives
<a name="objectives"></a>

This guide can help you achieve the following targeted business outcomes:
+ **Reduced costs** –** **Create a cost-effective image classification implementation that matches a business case
+ **Efficiency** – Use automation to deploy and maintain an image classification solution that matches a business case
+ **Strategy** – Determine whether customized model development fits your use case

## Attachments
<a name="attachments-3c71b76a-1e6e-4c69-b783-1676c6b7fb2d"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
