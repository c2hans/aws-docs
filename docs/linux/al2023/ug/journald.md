---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/journald.html
---

# `systemd` journal replaces `rsyslog`
<a name="journald"></a>

In AL2023 the logging system package has changed from AL2. AL2023 doesn't install `rsyslog` by default, so the text based log files such as `/var/log/messages` that were available in AL2 aren't available by default. The default configuration for AL2023 is `systemd-journal`, which can be examined using `journalctl`. Although `rsyslog` is an optional package in AL2023, we recommend the new `systemd` based `journalctl` interface and related packages. For more information, see the [`journalctl`](https://www.freedesktop.org/software/systemd/man/journalctl.html) manual page.

 The systmed journal equivalent to some commonly used syslog commands are covered in the following table.

| AL2 syslog command | AL2023 systemd journal equivalent |
| --- | --- |
| <pre>[ec2-user ~]$ cat /var/log/messages</pre> | <pre>[ec2-user ~]$ journalctl</pre> |
| <pre>[ec2-user ~]$ tail -f /var/log/messages</pre> | <pre>[ec2-user ~]$ journalctl -f</pre> |
| <pre>[ec2-user ~]$ grep foo /var/log/messages</pre> | <pre>[ec2-user ~]$ journalctl | grep foo</pre> |
