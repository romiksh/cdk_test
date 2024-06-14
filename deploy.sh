#!/usr/bin/env bash
if [[ $# -ge 3 ]]; then
    export CDK_DEPLOY_ACCOUNT=$2
    export CDK_DEPLOY_REGION=$3
    shift; shift
    cdk $1 "$@"
    exit $?
else
    echo 1>&2 "Provide deploy or bootstrap as first argument"
    echo 1>&2 "Provide Account as second argument"
    echo 1>&2 "Provide Region as third  args."
    echo 1>&2 "Additional args are passed through to cdk deploy."
    exit 1
fi