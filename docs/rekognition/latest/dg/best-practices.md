---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/best-practices.html
---

# Best practices for sensors, input images, and videos
<a name="best-practices"></a>

This section contains best practice information for using Amazon Rekognition. These best practices will help you get optimal performance out of the operations you invoke. If you are struggling to get the expected results from an operation, ensure you are following the best practices documented here.

For information regarding the latency of image operations, see the following:
+ [Amazon Rekognition Image operation latency](operation-latency.md)

Facial comparision and faces search operations require you to follow specific best practices to find faces in an image. These requirements have also been documented in the following link:
+ [Recommendations for facial comparison input images](recommendations-facial-input-images.md)
+ [Recomendations for searching faces in a collection](recommendations-facial-input-images-search.md)

The following sections cover how to set up your camera for each type of media Amazon Rekognition is capable of analyzing:
+ [Recommendations for camera setup (image and video)](recommendations-camera-image-video.md)
+ [Recommendations for camera setup (stored and streaming video)](recommendations-camera-stored-streaming-video.md)
+ [Recommendations for camera setup (streaming video)](recommendations-camera-streaming-video.md)

 The Face Liveness operations also have their own best practices that should be followed to get the best performance from the Liveness check tool:
+ [Recommendations for Usage of Face Liveness](recommendations-liveness.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
