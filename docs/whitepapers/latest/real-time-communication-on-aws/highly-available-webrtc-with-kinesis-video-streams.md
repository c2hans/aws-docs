---
source_url: https://docs.aws.amazon.com/whitepapers/latest/real-time-communication-on-aws/highly-available-webrtc-with-kinesis-video-streams.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Highly available WebRTC with Amazon Kinesis Video Streams
<a name="highly-available-webrtc-with-kinesis-video-streams"></a>

[Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/?nc=sn&loc=0&amazon-kinesis-video-streams-resources-blog.sort-by=item.additionalFields.createdDate&amazon-kinesis-video-streams-resources-blog.sort-order=desc) offers real-time media streaming via WebRTC, allowing users to capture, process, and store media streams for playback, analytics, and machine learning. These streams are highly available, scalable, and compliant with WebRTC standards. Amazon Kinesis Video Streams include a WebRTC signaling endpoint for fast peer discovery and secure connection establishment. It includes managed Session Traversal Utilities for NAT (STUN) and Traversal Using Relays around NAT (TURN) end-points for real-time exchange of media between peers. It also includes a free open-source SDK that directly integrates with camera firmware to enable secure communication with Amazon Kinesis Video Streams end-points, allowing for peer discovery and media streaming. Finally, it provides client libraries for Android, iOS, and JavaScript that allow WebRTC compliant mobile and web players to securely discover and connect with a camera device for media streaming and two-way communication.
