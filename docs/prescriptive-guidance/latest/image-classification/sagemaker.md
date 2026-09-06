---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/image-classification/sagemaker.html
---

# Amazon SageMaker AI endpoints
<a name="sagemaker"></a>

[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is a managed ML service that helps you build and train models and then deploy them into a production-ready hosted environment. Unlike Amazon SageMaker AI Canvas, you don't have the option of using a ready-to-use model in SageMaker AI. In SageMaker AI, you are responsible for providing the sample data and training the model. This provides you with more control but also more operational overhead and responsibility.

You can deploy a custom model in SageMaker AI as either a [real-time](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) or [serverless](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) endpoint. Alternatively, you can use [batch transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html), depending on your application demands. Even if a model will not be deployed as a SageMaker AI endpoint, the model artifact that SageMaker AI produces can be used for a customized deployment. For examples of SageMaker AI image classification models, see the following resources on GitHub:
+ [Amazon SageMaker JumpStart image classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart_image_classification/Amazon_JumpStart_Image_Classification.ipynb)
+ [Amazon SageMaker TensorFlow image classification](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_amazon_algorithms/image_classification_tensorflow/Amazon_TensorFlow_Image_Classification.ipynb)
+ [Amazon SageMaker multi-label image classification](https://sagemaker-examples-test-website.readthedocs.io/en/latest/introduction_to_amazon_algorithms/imageclassification_mscoco_multi_label/Image-classification-multilabel-lst.html)

After a model is trained, you can use SageMaker AI Neo to compile the model and make it more computationally efficient. Neo automatically optimizes Gluon, Keras, MXNet, PyTorch, TensorFlow, TensorFlow-Lite, and ONNX models for inference on Android, Linux, and Windows machines. For more information, see [Optimize model performance using Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html).

The following are the advantages of SageMaker AI:
+ Full control of model architecture, objective, and training procedure
+ Ability to select the instance type for your endpoint deployments
+ Ability to compile a model with SageMaker AI Neo for efficient deployment

The following are the disadvantages of SageMaker AI:
+ Manual setup requires more labor than automated approaches

For more information about SageMaker AI, see the following:
+ [Get started](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html) in the *SageMaker AI Developer Guide*
+ [Overview of machine learning with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html) in the *SageMaker AI Developer Guide*
