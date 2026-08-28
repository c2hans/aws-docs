---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/what-is-an-intrusion-method.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# What is an intrusion method?
<a name="what-is-an-intrusion-method"></a>

 Observation and analysis suggests that in traditional IT environments attackers often employ a repeatable process that helps them identify their target and potential weaknesses in their target’s security posture, as well as ways to exploit these weaknesses. Once the victim’s weaknesses are successfully exploited, attackers use illicit access to their victim’s infrastructure for a range of nefarious purposes, including data theft, compromising data integrity, destroying data and/or infrastructure, disrupting operations, and perpetrating attacks on other victims. The process that attackers use to conduct an attack can be analyzed as an *intrusion kill chain*. The terminology comes from military usage, where the series of steps required to attack a target is called a “chain,” and a successful attack is called a “kill.” While the terminology is rather military oriented for cybersecurity purposes, the concepts are well-established and many remain reasonably useful. For the purposes of this paper, we use “intrusion methods” interchangeably with “kill chains” when not specifically discussing a particular classic intrusion analysis framework.

 Attackers perform different tasks in each phase of their intrusion, as they plan and execute their intrusion attempts. In the mapping section, this paper modifies previous models slightly, so that organizations can leverage the inherent benefits of the cloud and the mitigations provided by AWS to stop intrusions.

## Phases of Lockheed Martin Framework
<a name="phases-of-lockheed-martin-framework"></a>

 The Lockheed Martin “kill chain” framework breaks down attacker behavior into the following phases:

### Phase 1: Reconnaissance
<a name="phase-1-reconnaissance-pre-intrusion"></a>

 This phase represents the work attackers do to research and select their targets, and understand their targets’ digital footprints. These activities include port scans and vulnerability scans of publicly accessible systems of the targets and their supply chain partners.

### Phase 2: Weaponization (Exploit Development)
<a name="phase-3-weaponization-exploit-development"></a>

 In this phase, attackers plan and acquire the tools they’ll use to try to exploit the weaknesses they believe the victim has. For example, they may build a malformed PDF file that is specially crafted to exploit a vulnerability in a PDF parser they know their intended victim uses. Attackers may also develop malware to steal system login credentials from the victim. (Note that this document hereafter refers to this phase as *exploit development* rather than weaponization.)

### Phase 3: Delivery
<a name="phase-4-delivery"></a>

 In this phase, the attackers transmit their *weapon* to the intended victim. Examples of delivery mechanisms include phishing emails, malicious email attachments, drive-by download sites, and so on.

### Phase 4: Exploitation
<a name="phase-5-exploitation"></a>

 After being delivered to the target, the *weapon* seeks to exploit the weakness it was designed for. This weakness may be a vulnerability or misconfiguration in an operating system, web browser, or other application. An exploit can also be designed to trick people into making poor trust decisions—also known as *social engineering*. Another weakness that attackers typically try to exploit is weak, leaked, or stolen passwords or other types of credentials.

### Phase 5: Installation
<a name="phase-6-installation"></a>

 After vulnerabilities have been successfully exploited, many attackers attempt to persist undetected in the environment as long as possible to accomplish their objectives. In this phase, attackers attempt to install tools that allow them to maintain running code and remote access to that code inside the victim’s environment.

### Phase 6: Command and Control
<a name="phase-7-command-and-control"></a>

 Attackers maintain illicit access to their victims’ environments and potentially remotely control compromised infrastructure.

### Phase 7: Actions on Objectives
<a name="phase-8-actions-on-objectives"></a>

 At this point in the intrusion (or earlier, depending on the chosen methods), the attackers are in a position to achieve their objectives. Objectives can include data theft, compromising data integrity, destroying data and/or infrastructure, disrupting operations, and perpetrating attacks on other victims.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
