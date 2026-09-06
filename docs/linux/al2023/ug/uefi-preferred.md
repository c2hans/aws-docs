---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/uefi-preferred.html
---

# UEFI Preferred and Secure Boot
<a name="uefi-preferred"></a>

By default, any instances launched with the AL2023 AMI on instance types that support UEFI firmware will launch in UEFI mode. This is done by setting the Boot Mode AMI parameter to `uefi-preferred`. For more information, see [ Boot Modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the *Amazon EC2 User Guide*.

 On Amazon EC2 instance types that support UEFI Secure Boot, it is possible to enable Secure Boot in Amazon Linux 2023. For more information, see [UEFI Secure Boot on AL2023](uefi-secure-boot.md).
