---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-s2110-pull.html
---

# Channel input—SMPTE 2110 input
<a name="input-s2110-pull"></a>

To verify that the input is set up correctly, look at the **SMPTE 2110 Receiver Group** section. It shows information from the SDP files that you specified when you created the input. For example:
+ **Video SDP: http://172.18.8.19/curling\_video.sdp, Media index: 2**
+ **Audio SDPs: http://172.18.8.19/curling\_audio\_1.sdp, Media index: 0**
  + **http://172.18.8.19/curling\_audio\_2.sdp, Media index: 0**
  + **http://172.18.8.19/curling\_audio\_2.sdp, Media index: 1**
+ **Ancillary SDPs: http://172.18.8.19/curling\_ancill.sdp, Media index: 0**

  **Ancillary SDPs: http://172.18.8.19/curling\_ancill.sdp, Media index: 1**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
