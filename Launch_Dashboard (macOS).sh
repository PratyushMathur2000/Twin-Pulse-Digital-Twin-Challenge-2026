#!/usr/bin/env bash
DIR="$(cd "$(dirname "$0")" && pwd)"
open "$DIR/twin_pulse_clinical_dashboard.html" || xdg-open "$DIR/twin_pulse_clinical_dashboard.html"
