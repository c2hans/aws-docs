---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers.html
---

# Improve call quality on agent workstations in Amazon Connect contact centers
<a name="improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers"></a>

*Ernest Ozdoba, Amazon Web Services*

## Summary
<a name="improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers-summary"></a>

Call quality issues are some of the most difficult problems to troubleshoot in contact centers. To avoid voice quality issues and complex troubleshooting procedures, you must optimize your agents’ work environment and workstation settings. This pattern describes voice quality optimization techniques for agent workstations in Amazon Connect contact centers. It provides recommendations in the following areas:
+ Work environment adjustments. Agents’ surroundings don’t affect how voice is transmitted over the network, but they do have an effect on call quality.
+ Agent workstation settings. Hardware and network configurations for contact center workstations have significant effects on call quality.
+ Browser settings. Agents use a web browser to access the Amazon Connect Contact Control Panel (CCP) website and communicate with customers, so browser settings can affect call quality.

The following components can also affect call quality, but they fall outside the scope of the workstation and aren’t covered in this pattern:
+ Traffic flows to the Amazon Web Services (AWS) Cloud over AWS Direct Connect, a full-tunnel VPN, or a split-tunnel VPN
+ Network conditions when working in or outside the corporate office
+ Public switched telephone network (PSTN) connectivity
+ The customer’s device and telephony carrier
+ Virtual desktop infrastructure (VDI) setup

For more information relating to these areas, see [Common Contact Control Panel (CCP) Issues](https://docs.aws.amazon.com/connect/latest/adminguide/common-ccp-issues.html) and [Use the Endpoint Test Utility](https://docs.aws.amazon.com/connect/latest/adminguide/check-connectivity-tool.html) in the Amazon Connect documentation.

## Prerequisites and limitations
<a name="improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers-prereqs"></a>

**Prerequisites**
+ Headsets and workstations must comply with the requirements specified in the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/ccp-agent-hardware.html).

**Limitations**
+ The optimization techniques in this pattern apply to soft phone voice quality. They do not apply when you configure the Amazon Connect CCP in desk phone mode. However, you can use desk phone mode if your soft phone setup doesn’t provide acceptable voice quality for the call.

**Product versions**
+ For supported browsers and versions, see the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/browsers.html).

## Architecture
<a name="improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers-architecture"></a>

This pattern is architecture-agnostic because it targets agent workstation settings. As the following diagram shows, the voice path from the agent to the customer is affected by the agent’s headset, browser, operating system, workstation hardware, and network.

![Voice path from agent to customer in Amazon Connect workstation calls](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/04ac4c80-30c4-4a48-8411-e3aac7bc2887/images/04e94efc-39d1-424d-a299-89ea17d40153.png)

In Amazon Connect contact centers, the user’s audio connectivity is established with WebRTC. Voice is encoded with the [Opus interactive audio codec](https://opus-codec.org/) and encrypted with the Secure Real-time Transport Protocol (SRTP) in transit. Other network architectures are possible, including VPN, private WAN/LAN, and ISP networks.

## Tools
<a name="improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers-tools"></a>
+ [Amazon Connect Endpoint Test Utility](https://tools.connect.aws/endpoint-test/) – This utility checks network connectivity and browser settings.
+ Browser configuration editors for WebRTC settings:
  + For Firefox: **about:config**
  + For Chrome: **chrome://flags**
+ [CCP Log Parser ](https://tools.connect.aws/ccp-log-parser/index.html)– This tool helps you analyze CCP logs for troubleshooting purposes.

## Epics
<a name="improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers-epics"></a>

### Adjust the work environment
<a name="adjust-the-work-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Reduce background noise. | Avoid noisy environments. If this is not possible, optimize the environment with these soundproofing tips:+ Absorb noise by using sound-dissipating surfaces such as curtains, carpets, and soft furnishings.<br />+ Block noise by putting barriers between desks.<br />+ Consider an active noise cancellation (ANC) solution such as a white noise generator to help concentration and ensure privacy, or use noise-canceling headsets.<br />+ Prevent echo on your calls. Big, empty spaces might create echo effects or amplify noises. Covering surfaces that can bounce sounds will help reduce echoes. | Agent, Manager |

### Optimize agent workstation settings
<a name="optimize-agent-workstation-settings"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Choose the right headset. | + If the environment is noisy, choose a stereo headset. Directing sound to both ears helps agents focus and hear the customer better, and reduces the overall noise by making it less likely for agents to raise their voices.<br />+ Avoid using loud speakers or built-in computer audio. For best quality, use a wired headset that’s dedicated to contact center use. Wireless headsets are convenient, but they might be a source of additional audio delay and reduced audio quality because of radio interference and transcoding. | Agent, Manager |
| Use the headset as intended. | + Enable the active noise canceling and speech enhancement features of your headset if they are available. Look for settings such as ANC or ANR. For instructions on activating these settings, see the user manual for your headset.<br />+ Adjust your microphone so you can speak directly into it. The best position for your microphone is just below your chin. Correct placement can make a difference of 10 decibels (dB) in the sound level. Most headsets allow you to rotate or bend the microphone arm (boom), so it is important to keep it in the right place when you are talking. <br />+ Some headsets are equipped with multiple microphones and advanced features such as voice beamforming, which helps capture speech without a boom. To make sure that you’re using the main microphone as intended by the manufacturer, see the user manual for your device. | Agent |
| Check workstation resources. | Make sure that your agents’ computers are performant. If they use third-party applications that consume resources, their computers might not meet the minimum [hardware requirements](https://docs.aws.amazon.com/connect/latest/adminguide/ccp-agent-hardware.html) to run CCP. If agents experience call quality issues, make sure that they have enough processing power (CPU), disk space, network bandwidth, and memory available for CCP. Agents should close any unnecessary applications and tabs to improve CCP performance and call quality. | Administrator |
| Configure the operating system’s sound settings. | The default settings for microphone level and boost usually work fine. If you find that outbound voice is quiet or the microphone is picking up too much, it might help to adjust these settings. Microphone settings can be found in your computer’s system sound configuration (**Sound**, **Input** on [MacOS](https://support.apple.com/en-gb/guide/mac-help/mchlp2567/12.0/mac/12.0), **Microphone Properties** in [Windows](https://support.microsoft.com/en-us/windows/fix-microphone-problems-5f230348-106d-bfa4-1db5-336f35576011)). You can access advanced settings that might affect voice quality through system tools or third-party applications. Here are some of the settings you can check:+ Sample rate – This value determines how many times the sound is probed per second. The default setting is usually 44 or 48 kilohertz (kHz). The optimal value for Amazon Connect is 48 kHz. You can use your browser settings to override the default value. For more information, see the [troubleshooting section](https://docs.aws.amazon.com/connect/latest/adminguide/verify-sample-rate.html) of the *Amazon Connect Administrator Guide*.<br />+ Gain – This value determines how much the microphone amplifies the sound. If you turn the gain up, your microphone might pick up more background noise. <br />+ Bit depth – This digital resolution value describes how many levels of sound amplitude are being recognized. The higher the bit depth, the smoother the voice sounds. However, many traditional telephony networks use the pulse-code modulation (PCM) standard, which supports only 8-bit resolution.<br />+ Open threshold – This is the minimal sound amplitude that a microphone picks up. <br />If you’re experiencing voice quality issues, try restoring these values to their default settings before investigating further.<br />For more information about these and other adjustable settings, see your device manual. | Agent, Administrator |
| Use a wired network. | Typically, wired ethernet has lower latency, so it is easier to provide the consistent transmission quality required for voice data transmission.  We recommend 100 KB bandwidth per call at the minimum. + If agents are working from home, we recommend wired over wireless connections. It shouldn’t take more than 150 milliseconds to hear the customer. You can access Amazon Connect’s latency test from the [Amazon Connect Endpoint Test Utility](https://tools.connect.aws/endpoint-test/). However, this utility measures the delay from the browser to Amazon Connect Regions, not to customers. The 150-millisecond one-way delay recommendation prevents the agent and customer from talking over each other. The value is measured from end to end, and each element adds a delay, including the part of the call between the Amazon Connect Region and the customer.<br />+ If agents are working from the office, corporate Wi-Fi is acceptable as long as parameters are in the recommended range, and Real-time Transport Protocol (RTP) traffic is prioritized. | Network administrator, Agent |
| Update hardware drivers. | When you use a USB or other type of headset that has its own firmware, we recommend that you keep it updated with the latest version. Simple headsets that use an auxiliary port use the computer’s built-in audio device, so make sure that the operating system hardware driver is up to date. In rare cases, an audio driver update can cause audio issues, and you might need to roll it back. For more information about changing firmware and driver versions, see your device manual. | Administrator |
| Avoid USB hubs and dongles. | When you connect your headset, avoid additional devices such as dongles, port type converters, hubs, and extension cables.<br />These devices might affect call quality. Connect your device directly to the port in your computer instead. | Agent |
| Check CCP logs. | The CCP Log Parser provides an easy way to check application logs.1. [Download the CCP logs](https://docs.aws.amazon.com/connect/latest/adminguide/download-ccp-logs.html) after a call.<br />2. Open the [CCP Log Parser](https://tools.connect.aws/ccp-log-parser/index.html).<br />3. Drag and drop the log file to upload the log for analysis.<br />4. When the log has been analyzed, the **Snapshots & Logs** tab will be selected by default. Choose the **Metrics** tab next to it to check insights.<br />5. In the **WebRTC Metrics - audio\_input **section, check the following:The **Audio Level** graph, to see if your received audio level is above 0. This indicates that audio was received from your caller.The **Packets** graph for any lost packets. If this chart shows significant increases, contact your IT support team.<br />6. In the **WebRTC Metrics - audio\_output **section, check the following:The **Audio Level** graph, to confirm that audio was sent out from your device.The **Packets** graph. If you see a packet loss spike, report it to your IT support team.The **Jitter Buffer & RTT** graph. Round trip time (RTT) values above 300 will affect the call experience. Report these to your IT support team. | Agent (advanced skills) |

### Optimize browser settings
<a name="optimize-browser-settings"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Restore default WebRTC settings. | WebRTC has to be enabled to make soft phone calls with CCP. We recommend that you keep the default settings for WebRTC-related features. + In Chrome, you can set flags by navigating to the URL **chrome://flags**. Type **WebRTC** in the search box to find settings that can interfere with CCP, and set these to **Default**. <br />+ In Firefox, type **about:config** in the address bar, and then type **WebRTC** in the search box on the configuration page. Non-default settings appear in bold text and can be changed to **Default**. | Administrator |
| Disable browser extensions when troubleshooting. | Some browser extensions might affect call quality or even prevent calls from connecting properly. Use the incognito window or private mode in your browser, and disable all extensions. If that solves the problem, review your browser extensions and look for suspicious add-ons, or disable them individually. | Agent, Administrator |
| Check the browser sample rate.  | Confirm that your microphone input is set to the optimal 48 kHz sample rate. For instructions, see the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/verify-sample-rate.html). | Agent, Administrator |

## Related resources
<a name="improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers-resources"></a>

If you’ve followed the steps in this pattern but you’re still encountering problems with call quality, see the following resources for troubleshooting tips.
+ Review [common Contact Control Panel (CCP) issues](https://docs.aws.amazon.com/connect/latest/adminguide/common-ccp-issues.html).
+ Check the connection with the [Endpoint Test Utility](https://docs.aws.amazon.com/en_us/connect/latest/adminguide/check-connectivity-tool.html).
+ Follow the [troubleshooting guide ](https://docs.aws.amazon.com/connect/latest/adminguide/troubleshooting.html)for any other issues.

If your troubleshooting and adjustments don’t solve the call quality issue, the root cause might be external to your workstation. For further troubleshooting, contact your IT support team.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
