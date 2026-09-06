---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/cron.html
---

# `systemd` timers replace `cron`
<a name="cron"></a>

The `cronie` package was installed by default on the AL2 AMI, providing support for the traditional `crontab` way of scheduling periodic tasks. In AL2023, `cronie` is not included by default. Therefore, support for `crontab` is no longer provided by default.

You can optionally install the `cronie` package to use classic `cron` jobs. We recommend that you migrate to `systemd` timers due to the added functionality provided by `systemd`.
