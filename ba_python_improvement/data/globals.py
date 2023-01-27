from nornir import InitNornir

global SELECTED_DEVICES
SELECTED_DEVICES=""

global NORNIR_INIT
NORNIR_INIT = InitNornir(config_file="data/config.yml")
