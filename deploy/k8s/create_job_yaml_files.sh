#!/bin/bash
#
base_path=$1
build_id=$2
#
mkdir -p "$base_path/yamls"
#
while IFS=',' read -r jobname taskname schedule; do
  if [[ "$jobname" != "jobname" ]]; then # Skip the titles line
    sed \
    -e "s|\${jobname}|$jobname|" \
    -e "s|\${taskname}|$taskname|" \
    -e "s|\${schedule}|$schedule|" \
    -e "s|\${buildid}|$build_id|" \
    "$base_path/job_template.yaml" > "$base_path/yamls/cronjob_$jobname.yaml"
  fi
done < "$base_path/jobs.csv"