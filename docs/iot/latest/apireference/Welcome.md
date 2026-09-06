---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

## AWS IoT
<a name="Welcome_AWS_IoT"></a>

 AWS IoT provides secure, bi-directional communication between Internet-connected devices (such as sensors, actuators, embedded devices, or smart appliances) and the AWS cloud. You can discover your custom IoT-Data endpoint to communicate with, configure rules for data processing and integration with other services, organize resources associated with each device (Registry), configure logging, and create and manage policies and credentials to authenticate devices.

The service endpoints that expose this API are listed in [AWS IoT Core Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html). You must use the endpoint for the region that has the resources you want to access.

The service name used by [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to sign the request is: *execute-api*.

For more information about how AWS IoT works, see the [Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-how-it-works.html).

For information about how to use the credentials provider for AWS IoT, see [Authorizing Direct Calls to AWS Services](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html).

## AWS IoT data
<a name="Welcome_AWS_IoT_Data_Plane"></a>

 AWS IoT data enables secure, bi-directional communication between Internet-connected things (such as sensors, actuators, embedded devices, or smart appliances) and the AWS cloud. It implements a broker for applications and things to publish messages over HTTP (Publish) and retrieve, update, and delete shadows. A shadow is a persistent representation of your things and their state in the AWS cloud.

Find the endpoint address for actions in AWS IoT data by running this CLI command:

 `aws iot describe-endpoint --endpoint-type iot:Data-ATS`

The service name used by [AWSSignature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to sign requests is: *iotdevicegateway*.

## AWS IoT jobs data
<a name="Welcome_AWS_IoT_Jobs_Data_Plane"></a>

 AWS IoT Jobs is a service that allows you to define a set of jobs — remote operations that are sent to and executed on one or more devices connected to AWS IoT Core. For example, you can define a job that instructs a set of devices to download and install application or firmware updates, reboot, rotate certificates, or perform remote troubleshooting operations.

Find the endpoint address for actions in the AWS IoT jobs data plane by running this CLI command:

 `aws iot describe-endpoint --endpoint-type iot:Jobs`

The service name used by [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to sign requests is: *iot-jobs-data*.

 To create a job, you make a job document which is a description of the remote operations to be performed, and you specify a list of targets that should perform the operations. The targets can be individual things, thing groups or both.

 AWS IoT Jobs sends a message to inform the targets that a job is available. The target starts the execution of the job by downloading the job document, performing the operations it specifies, and reporting its progress to AWS IoT Core. The Jobs service provides commands to track the progress of a job on a specific target and for all the targets of the job

## AWS IoT Core Device Advisor
<a name="Welcome_AWS_IoT_Core_Device_Advisor"></a>

 AWS IoT Core Device Advisor is a cloud-based, fully managed test capability for validating IoT devices during device software development. Device Advisor provides pre-built tests that you can use to validate IoT devices for reliable and secure connectivity with AWS IoT Core before deploying devices to production. By using Device Advisor, you can confirm that your devices can connect to AWS IoT Core, follow security best practices and, if applicable, receive software updates from IoT Device Management. You can also download signed qualification reports to submit to the AWS Partner Network to get your device qualified for the AWS Partner Device Catalog without the need to send your device in and wait for it to be tested.

## AWS IoT Secure Tunneling
<a name="Welcome_AWS_IoT_Secure_Tunneling"></a>

 AWS IoT Secure Tunneling creates remote connections to devices deployed in the field.

For more information about how AWS IoT Secure Tunneling works, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html).
