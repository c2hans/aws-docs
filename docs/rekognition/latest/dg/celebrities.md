---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/celebrities.html
---

# Recognizing celebrities
<a name="celebrities"></a>

Amazon Rekognition makes it easy for customers to automatically recognize tens of thousands of well-known personalities in images and videos using machine learning. The metadata provided by the celebrity recognition API significantly reduces the repetitive manual effort required to tag content and make it readily searchable.

The rapid proliferation of image and video content means that media companies often struggle to organize, search, and utilize their media catalogs at scale. News channels and sports broadcasters often need to find images and videos quickly, in order to respond to current events and create relevant programming. Insufficient metadata makes these tasks difficult, but with Amazon Rekognition you can automatically tag large volumes of new or archival content to make it easily searchable for a comprehensive set of international, widely known celebrities like actors, sportspeople, and online content creators.

Amazon Rekognition celebrity recognition is designed to be used exclusively in cases where you expect there may be a known celebrity in an image or a video. For information about recognizing faces that are not celebrities, see [Searching faces in a collection](collections.md).

**Note**
If you are a celebrity and don’t want to be included in this feature, contact [AWS Support](https://aws.amazon.com/contact-us/) or email rekognition-celebrity-opt-out@amazon.com.

**Topics**
+ [Celebrity recognition compared to face search](celebrity-recognition-vs-face-search.md)
+ [Recognizing celebrities in an image](celebrities-procedure-image.md)
+ [Recognizing celebrities in a stored video](celebrities-video-sqs.md)
+ [Getting information about a celebrity](get-celebrity-info-procedure.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
