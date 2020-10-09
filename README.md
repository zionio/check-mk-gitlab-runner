# check-mk-gitlab-runner

This is a very simple local check to show GitLab Runner status.

## Install

### Check_MK CRE (check-mk-raw)

Download `custom/gitlab_runner/lib/local/gitlab_runner` and copy
to `/usr/lib/check_mk_agent/plugins/` directory.

### Check_MK CEE (check-mk-enterprise)

The package can be distributed with [Agent Backery](https://checkmk.com/cms_wato_monitoringagents.html)

* Download [latest release](https://github.com/zionio/check-mk-gitlab-runner/releases)
and upload with [Extension Packages](https://checkmk.com/cms_mkps.html)
* Go to _Monitoring Agents_ -> _Rules_ -> _Generic Options_ -> _Deploy custom files with agent_
and create (or edit) a Rule.
