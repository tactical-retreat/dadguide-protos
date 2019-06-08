///
//  Generated code. Do not modify.
//  source: monster.proto
///
// ignore_for_file: camel_case_types,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name

const MonsterType$json = const {
  '1': 'MonsterType',
  '2': const [
    const {'1': 'UNKNOWN_MONSTER_TYPE', '2': 0},
    const {'1': 'GOD', '2': 1},
    const {'1': 'WORK', '2': 2},
  ],
};

const Awakening$json = const {
  '1': 'Awakening',
  '2': const [
    const {'1': 'UNKNOWN_AWAKENING', '2': 0},
    const {'1': 'HP_BOOST', '2': 1},
  ],
};

const CrossServerInt$json = const {
  '1': 'CrossServerInt',
  '2': const [
    const {'1': 'jp', '3': 1, '4': 1, '5': 5, '10': 'jp'},
    const {'1': 'na', '3': 2, '4': 1, '5': 5, '10': 'na'},
    const {'1': 'kr', '3': 3, '4': 1, '5': 5, '10': 'kr'},
  ],
};

const CrossServerString$json = const {
  '1': 'CrossServerString',
  '2': const [
    const {'1': 'jp', '3': 1, '4': 1, '5': 9, '10': 'jp'},
    const {'1': 'na', '3': 2, '4': 1, '5': 9, '10': 'na'},
    const {'1': 'kr', '3': 3, '4': 1, '5': 9, '10': 'kr'},
  ],
};

const Monster$json = const {
  '1': 'Monster',
  '2': const [
    const {'1': 'unique_id', '3': 1, '4': 1, '5': 5, '10': 'uniqueId'},
    const {'1': 'monster_id', '3': 2, '4': 1, '5': 11, '6': '.dadguide.CrossServerInt', '10': 'monsterId'},
    const {'1': 'name', '3': 3, '4': 1, '5': 11, '6': '.dadguide.CrossServerString', '10': 'name'},
    const {'1': 'type_1', '3': 4, '4': 1, '5': 14, '6': '.dadguide.MonsterType', '10': 'type1'},
    const {'1': 'type_2', '3': 5, '4': 1, '5': 14, '6': '.dadguide.MonsterType', '10': 'type2'},
    const {'1': 'type_3', '3': 6, '4': 1, '5': 14, '6': '.dadguide.MonsterType', '10': 'type3'},
    const {'1': 'awakenings', '3': 7, '4': 3, '5': 14, '6': '.dadguide.Awakening', '10': 'awakenings'},
    const {'1': 'super_awakenings', '3': 8, '4': 3, '5': 14, '6': '.dadguide.Awakening', '10': 'superAwakenings'},
  ],
};

