---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/connect-optimization.html
---

# Amazon Connect Customer Optimization for Amazon WorkSpaces
<a name="connect-optimization"></a>

The end user experience for contact center agents needs to be a top priority because if their audio is degraded, it creates a bad call experience for the customer they are serving. When running a contact center solution within a remote desktop, audio performance will always be impacted on some measurable scale when voice traffic is not prioritized over the network connection. This impact is due to the audio flowing from the audio endpoint to the virtual session and then being compressed over the streaming protocol to be delivered to the end user. This additional routing results in the audio to have degraded performance through network bottlenecks.

An approach to avoid this behavior is to split the audio out of session, meaning all of the contact center agent’s resources remain in-session while the audio stream stays out of the session. This split allows the audio to stream from the audio endpoint directly to the end user while all other call resources, including the PII the agent is viewing, to remain in a secure session. This audio optimization is considered a best practice since it ensures the customer’s call experience is as good as it can be.

[Amazon Connect Customer](https://aws.amazon.com/connect/) offers a [Streams API](https://github.com/amazon-connect/amazon-connect-streams) that allows administrators to customize their [Contact Control Panel](https://docs.aws.amazon.com/connect/latest/adminguide/launch-ccp.html) (CCP) to meet their business requirements. One of the options an administrator has is to control if the custom CCP can receive audio for the call. These settings allow us to configure a split CCP; an audio-only CCP for out of session and a media-less CCP for in-session. Once administrators have configured these custom CCPs, they are able to leverage [Amazon Connect audio optimization for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-amazon-connect-audio-optimization.html). Since CCPs are delivered within the browser, this setting allows administrators to provide their audio-only CCP URL to the WorkSpaces directory. Once configured, when WorkSpaces Connect contact center agents successfully authenticate to their WorkSpaces, the WorkSpaces client will automatically open the provided audio-only CCP URL in the agent’s local default browser. This action allows the audio to flow directly to the agent’s local machine while the media-less CCP handles everything else within the secure WorkSpaces session.

Architecture Diagram

![Image showing Connect Customer and WorkSpaces architecture](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/connect-workspaces-architecture.png)
