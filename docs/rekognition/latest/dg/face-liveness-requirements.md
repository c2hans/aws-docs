---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-requirements.html
---

# User-Side Face Liveness Requirements
<a name="face-liveness-requirements"></a>

Amazon Rekognition Face Liveness requires the following minimum specifications:

Devices:
+  Device must have a front-facing camera
+  Minimum refresh rate of the device display: 60 Hz
+  Minimum display or screen size: 4 inches
+  Device should not be jail-broken or rooted

Camera specifications:
+  Color Camera: front-facing camera should be able to record colors.
+  No virtual camera or camera software.
+  Minimum recording capability: 15 frames per second.
+  Minimum video recording resolution: 480x640px.
+  When users use a webcam with a desktop for a Face Liveness check, it is important to mount the webcam on top of the same screen where the Face Liveness check starts.

Minimum bandwidth requirement: 100 kbps

Browsers supported: Latest three versions of major browsers, such as Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge. For more information regarding browser support, see [What browsers are supported for use with the AWS Management Console?](https://aws.amazon.com/premiumsupport/knowledge-center/browsers-management-console/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
