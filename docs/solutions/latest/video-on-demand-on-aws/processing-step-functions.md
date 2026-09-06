---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/processing-step-functions.html
---

# Processing Step Functions
<a name="processing-step-functions"></a>

The solution uses the height and width of the source video to determine which job template to use to submit encoding jobs to MediaConvert. If you allow frame capture, the frame capture parameters are added to the job template. Then, the encoding job is created in MediaConvert and the details are stored in DynamoDB.
