---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-policies-cedar.html
---

# How Client VPN uses Cedar
<a name="device-posture-policies-cedar"></a>

A Client VPN authorization policy is made up of one or more Cedar `permit` and `forbid` statements. A connection is allowed only if it satisfies at least one `permit` statement and is not matched by any `forbid` statement. A `forbid` statement always takes precedence.

The following example permits a connection when the CrowdStrike overall assessment score is greater than 50.

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };
```

The following example combines a device signal with a user identity signal. It permits a connection only when the device has disk encryption enabled (a Jamf signal) and the user belongs to the `Engineering` SAML group.

```
permit(principal, action, resource)
when {
    context.jamf.diskEncryptionEnabled == true &&
    context.saml.memberOf.contains("Engineering")
};
```

The following example combines a `permit` statement with a `forbid` statement. It permits connections that meet the assessment score requirement, but always denies connections from devices that report a jailbroken state, regardless of any `permit` statement.

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };

forbid(principal, action, resource)
when { context.crowdstrike.jailbroken == true };
```
