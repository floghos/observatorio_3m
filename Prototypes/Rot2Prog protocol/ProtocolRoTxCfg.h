#include <settings_params_legacy.h>

#ifndef SPID_MD0X_PROTOCOLROTXCFG_H
#define SPID_MD0X_PROTOCOLROTXCFG_H


typedef enum rotCfgDataType: uint8_t {
	rcdt_MOTOR_INPUT,
	rcdt_MOTOR_KIND,
	rcdt_MOTOR_TYPE,
	rcdt_STATE,
	rcdt_float,
	rcdt_int32_t,
	rcdt_seComBaudRate,
	rcdt_seDataVersion,
	rcdt_seDisplayResolution,
	rcdt_seMotorControlPort,
	rcdt_seMotorControlProtocol,
	rcdt_seMotorShowAzimuth,
	rcdt_seMotorSoftStart,
	rcdt_seMotorTemplate,
	rcdt_uint16_t,
	rcdt_uint32_t,
	rcdt_uint8_t,
} rotCfgDataType;

typedef enum rotCfgDataTypeSimple: uint8_t {
	rcdts_uint8_t = 0,
	rcdts_uint16_t = 1,
	rcdts_uint32_t = 2,
	rcdts_float = 3,
	rcdts_int32_t = 4,
} rotCfgDataTypeSimple;

typedef struct rotCfgField {
    uint16_t fieldId;
    const char fieldName[32];
    void *fieldValue;
    rotCfgDataType dataType;
} rotCfgField;

static const rotCfgField rotCfgFields[] = {
	{1, "data_ver", &((ROT_FRAM_PARAMS *)(nullptr))->data_ver, rcdt_seDataVersion},
	{2, "motor_0_min_angle", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].min_angle, rcdt_float},
	{3, "motor_0_max_angle", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].max_angle, rcdt_float},
	{4, "motor_0_gear", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].gear, rcdt_float},
	{5, "motor_0_min_power", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].min_power, rcdt_uint8_t},
	{6, "motor_0_canEncoder", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].canEncoder, rcdt_uint16_t},
	{7, "motor_0_state", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].state, rcdt_STATE},
	{8, "motor_0_type", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].type, rcdt_MOTOR_TYPE},
	{9, "motor_0_kind", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].kind, rcdt_MOTOR_KIND},
	{10, "motor_0_input", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].input, rcdt_MOTOR_INPUT},
	{11, "motor_0_start_time_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].start_time[0], rcdt_uint8_t},
	{12, "motor_0_start_time_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].start_time[1], rcdt_uint8_t},
	{13, "motor_0_start_time_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].start_time[2], rcdt_uint8_t},
	{14, "motor_0_start_power_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].start_power[0], rcdt_uint8_t},
	{15, "motor_0_start_power_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].start_power[1], rcdt_uint8_t},
	{16, "motor_0_start_power_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].start_power[2], rcdt_uint8_t},
	{17, "motor_0_stop_time_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].stop_time[0], rcdt_uint8_t},
	{18, "motor_0_stop_time_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].stop_time[1], rcdt_uint8_t},
	{19, "motor_0_stop_time_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].stop_time[2], rcdt_uint8_t},
	{20, "motor_0_stop_power_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].stop_power[0], rcdt_uint8_t},
	{21, "motor_0_stop_power_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].stop_power[1], rcdt_uint8_t},
	{22, "motor_0_stop_power_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].stop_power[2], rcdt_uint8_t},
	{23, "motor_0_max_power", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].max_power, rcdt_uint8_t},
	{24, "motor_0_pulse_timeout", &((ROT_FRAM_PARAMS *)(nullptr))->motor[0].pulse_timeout, rcdt_uint8_t},
	{25, "motor_1_min_angle", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].min_angle, rcdt_float},
	{26, "motor_1_max_angle", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].max_angle, rcdt_float},
	{27, "motor_1_gear", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].gear, rcdt_float},
	{28, "motor_1_min_power", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].min_power, rcdt_uint8_t},
	{29, "motor_1_canEncoder", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].canEncoder, rcdt_uint16_t},
	{30, "motor_1_state", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].state, rcdt_STATE},
	{31, "motor_1_type", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].type, rcdt_MOTOR_TYPE},
	{32, "motor_1_kind", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].kind, rcdt_MOTOR_KIND},
	{33, "motor_1_input", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].input, rcdt_MOTOR_INPUT},
	{34, "motor_1_start_time_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].start_time[0], rcdt_uint8_t},
	{35, "motor_1_start_time_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].start_time[1], rcdt_uint8_t},
	{36, "motor_1_start_time_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].start_time[2], rcdt_uint8_t},
	{37, "motor_1_start_power_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].start_power[0], rcdt_uint8_t},
	{38, "motor_1_start_power_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].start_power[1], rcdt_uint8_t},
	{39, "motor_1_start_power_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].start_power[2], rcdt_uint8_t},
	{40, "motor_1_stop_time_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].stop_time[0], rcdt_uint8_t},
	{41, "motor_1_stop_time_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].stop_time[1], rcdt_uint8_t},
	{42, "motor_1_stop_time_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].stop_time[2], rcdt_uint8_t},
	{43, "motor_1_stop_power_0", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].stop_power[0], rcdt_uint8_t},
	{44, "motor_1_stop_power_1", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].stop_power[1], rcdt_uint8_t},
	{45, "motor_1_stop_power_2", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].stop_power[2], rcdt_uint8_t},
	{46, "motor_1_max_power", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].max_power, rcdt_uint8_t},
	{47, "motor_1_pulse_timeout", &((ROT_FRAM_PARAMS *)(nullptr))->motor[1].pulse_timeout, rcdt_uint8_t},
	{48, "com_0_baud", &((ROT_FRAM_PARAMS *)(nullptr))->com[0].baud, rcdt_seComBaudRate},
	{49, "com_0_data_bits", &((ROT_FRAM_PARAMS *)(nullptr))->com[0].data_bits, rcdt_uint8_t},
	{50, "com_0_stop_bits", &((ROT_FRAM_PARAMS *)(nullptr))->com[0].stop_bits, rcdt_uint8_t},
	{51, "com_0_parity", &((ROT_FRAM_PARAMS *)(nullptr))->com[0].parity, rcdt_uint8_t},
	{52, "com_1_baud", &((ROT_FRAM_PARAMS *)(nullptr))->com[1].baud, rcdt_seComBaudRate},
	{53, "com_1_data_bits", &((ROT_FRAM_PARAMS *)(nullptr))->com[1].data_bits, rcdt_uint8_t},
	{54, "com_1_stop_bits", &((ROT_FRAM_PARAMS *)(nullptr))->com[1].stop_bits, rcdt_uint8_t},
	{55, "com_1_parity", &((ROT_FRAM_PARAMS *)(nullptr))->com[1].parity, rcdt_uint8_t},
	{56, "motors_pulses_0", &((ROT_FRAM_PARAMS *)(nullptr))->motors.pulses[0], rcdt_int32_t},
	{57, "motors_pulses_1", &((ROT_FRAM_PARAMS *)(nullptr))->motors.pulses[1], rcdt_int32_t},
	{58, "motors_spin_0", &((ROT_FRAM_PARAMS *)(nullptr))->motors.spin[0], rcdt_uint8_t},
	{59, "motors_spin_1", &((ROT_FRAM_PARAMS *)(nullptr))->motors.spin[1], rcdt_uint8_t},
	{60, "motors_pins", &((ROT_FRAM_PARAMS *)(nullptr))->motors.pins, rcdt_uint8_t},
	{61, "motors_old_pins", &((ROT_FRAM_PARAMS *)(nullptr))->motors.old_pins, rcdt_uint8_t},
	{62, "motors_show_toPulses", &((ROT_FRAM_PARAMS *)(nullptr))->motors.show_toPulses, rcdt_uint8_t},
	{63, "motor_pins", &((ROT_FRAM_PARAMS *)(nullptr))->motor_pins, rcdt_uint32_t},
	{64, "manual_ctrl_start", &((ROT_FRAM_PARAMS *)(nullptr))->manual_ctrl_start, rcdt_seMotorSoftStart},
	{65, "manual_ctrl_stop", &((ROT_FRAM_PARAMS *)(nullptr))->manual_ctrl_stop, rcdt_seMotorSoftStart},
	{66, "usb_baudrate", &((ROT_FRAM_PARAMS *)(nullptr))->usb_baudrate, rcdt_seComBaudRate},
	{67, "use_short_way", &((ROT_FRAM_PARAMS *)(nullptr))->use_short_way, rcdt_STATE},
	{68, "satellite_mode", &((ROT_FRAM_PARAMS *)(nullptr))->satellite_mode, rcdt_STATE},
	{69, "displayResolution", &((ROT_FRAM_PARAMS *)(nullptr))->displayResolution, rcdt_seDisplayResolution},
	{70, "mouse_control", &((ROT_FRAM_PARAMS *)(nullptr))->mouse_control, rcdt_STATE},
	{71, "usb_state", &((ROT_FRAM_PARAMS *)(nullptr))->usb_state, rcdt_STATE},
	{72, "eth_state", &((ROT_FRAM_PARAMS *)(nullptr))->eth_state, rcdt_STATE},
	{73, "motor_template", &((ROT_FRAM_PARAMS *)(nullptr))->motor_template, rcdt_seMotorTemplate},
	{74, "motor_control1", &((ROT_FRAM_PARAMS *)(nullptr))->motor_control1, rcdt_seMotorControlPort},
	{75, "motor_protocol1", &((ROT_FRAM_PARAMS *)(nullptr))->motor_protocol1, rcdt_seMotorControlProtocol},
	{76, "motor_control2", &((ROT_FRAM_PARAMS *)(nullptr))->motor_control2, rcdt_seMotorControlPort},
	{77, "motor_protocol2", &((ROT_FRAM_PARAMS *)(nullptr))->motor_protocol2, rcdt_seMotorControlProtocol},
	{78, "com_state_0", &((ROT_FRAM_PARAMS *)(nullptr))->com_state[0], rcdt_STATE},
	{79, "com_state_1", &((ROT_FRAM_PARAMS *)(nullptr))->com_state[1], rcdt_STATE},
	{80, "az_show_math", &((ROT_FRAM_PARAMS *)(nullptr))->az_show_math, rcdt_seMotorShowAzimuth},
	{81, "pair_rotors", &((ROT_FRAM_PARAMS *)(nullptr))->pair_rotors, rcdt_STATE},
};


#endif //SPID_MD0X_PROTOCOLROTXCFG_H