///
//  Generated code. Do not modify.
//  source: monster.proto
///
// ignore_for_file: camel_case_types,non_constant_identifier_names,library_prefixes,unused_import,unused_shown_name

import 'dart:core' as $core show bool, Deprecated, double, int, List, Map, override, String;

import 'package:protobuf/protobuf.dart' as $pb;

import 'monster.pbenum.dart';

export 'monster.pbenum.dart';

class CrossServerInt extends $pb.GeneratedMessage {
  static final $pb.BuilderInfo _i = $pb.BuilderInfo('CrossServerInt', package: const $pb.PackageName('dadguide'))
    ..a<$core.int>(1, 'jp', $pb.PbFieldType.O3)
    ..a<$core.int>(2, 'na', $pb.PbFieldType.O3)
    ..a<$core.int>(3, 'kr', $pb.PbFieldType.O3)
    ..hasRequiredFields = false
  ;

  CrossServerInt() : super();
  CrossServerInt.fromBuffer($core.List<$core.int> i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) : super.fromBuffer(i, r);
  CrossServerInt.fromJson($core.String i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) : super.fromJson(i, r);
  CrossServerInt clone() => CrossServerInt()..mergeFromMessage(this);
  CrossServerInt copyWith(void Function(CrossServerInt) updates) => super.copyWith((message) => updates(message as CrossServerInt));
  $pb.BuilderInfo get info_ => _i;
  static CrossServerInt create() => CrossServerInt();
  CrossServerInt createEmptyInstance() => create();
  static $pb.PbList<CrossServerInt> createRepeated() => $pb.PbList<CrossServerInt>();
  static CrossServerInt getDefault() => _defaultInstance ??= create()..freeze();
  static CrossServerInt _defaultInstance;

  $core.int get jp => $_get(0, 0);
  set jp($core.int v) { $_setSignedInt32(0, v); }
  $core.bool hasJp() => $_has(0);
  void clearJp() => clearField(1);

  $core.int get na => $_get(1, 0);
  set na($core.int v) { $_setSignedInt32(1, v); }
  $core.bool hasNa() => $_has(1);
  void clearNa() => clearField(2);

  $core.int get kr => $_get(2, 0);
  set kr($core.int v) { $_setSignedInt32(2, v); }
  $core.bool hasKr() => $_has(2);
  void clearKr() => clearField(3);
}

class CrossServerString extends $pb.GeneratedMessage {
  static final $pb.BuilderInfo _i = $pb.BuilderInfo('CrossServerString', package: const $pb.PackageName('dadguide'))
    ..aOS(1, 'jp')
    ..aOS(2, 'na')
    ..aOS(3, 'kr')
    ..hasRequiredFields = false
  ;

  CrossServerString() : super();
  CrossServerString.fromBuffer($core.List<$core.int> i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) : super.fromBuffer(i, r);
  CrossServerString.fromJson($core.String i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) : super.fromJson(i, r);
  CrossServerString clone() => CrossServerString()..mergeFromMessage(this);
  CrossServerString copyWith(void Function(CrossServerString) updates) => super.copyWith((message) => updates(message as CrossServerString));
  $pb.BuilderInfo get info_ => _i;
  static CrossServerString create() => CrossServerString();
  CrossServerString createEmptyInstance() => create();
  static $pb.PbList<CrossServerString> createRepeated() => $pb.PbList<CrossServerString>();
  static CrossServerString getDefault() => _defaultInstance ??= create()..freeze();
  static CrossServerString _defaultInstance;

  $core.String get jp => $_getS(0, '');
  set jp($core.String v) { $_setString(0, v); }
  $core.bool hasJp() => $_has(0);
  void clearJp() => clearField(1);

  $core.String get na => $_getS(1, '');
  set na($core.String v) { $_setString(1, v); }
  $core.bool hasNa() => $_has(1);
  void clearNa() => clearField(2);

  $core.String get kr => $_getS(2, '');
  set kr($core.String v) { $_setString(2, v); }
  $core.bool hasKr() => $_has(2);
  void clearKr() => clearField(3);
}

class Monster extends $pb.GeneratedMessage {
  static final $pb.BuilderInfo _i = $pb.BuilderInfo('Monster', package: const $pb.PackageName('dadguide'))
    ..a<$core.int>(1, 'uniqueId', $pb.PbFieldType.O3)
    ..a<CrossServerInt>(2, 'monsterId', $pb.PbFieldType.OM, CrossServerInt.getDefault, CrossServerInt.create)
    ..a<CrossServerString>(3, 'name', $pb.PbFieldType.OM, CrossServerString.getDefault, CrossServerString.create)
    ..e<MonsterType>(4, 'type1', $pb.PbFieldType.OE, MonsterType.UNKNOWN_MONSTER_TYPE, MonsterType.valueOf, MonsterType.values)
    ..e<MonsterType>(5, 'type2', $pb.PbFieldType.OE, MonsterType.UNKNOWN_MONSTER_TYPE, MonsterType.valueOf, MonsterType.values)
    ..e<MonsterType>(6, 'type3', $pb.PbFieldType.OE, MonsterType.UNKNOWN_MONSTER_TYPE, MonsterType.valueOf, MonsterType.values)
    ..pc<Awakening>(7, 'awakenings', $pb.PbFieldType.PE, null, Awakening.valueOf, Awakening.values)
    ..pc<Awakening>(8, 'superAwakenings', $pb.PbFieldType.PE, null, Awakening.valueOf, Awakening.values)
    ..hasRequiredFields = false
  ;

  Monster() : super();
  Monster.fromBuffer($core.List<$core.int> i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) : super.fromBuffer(i, r);
  Monster.fromJson($core.String i, [$pb.ExtensionRegistry r = $pb.ExtensionRegistry.EMPTY]) : super.fromJson(i, r);
  Monster clone() => Monster()..mergeFromMessage(this);
  Monster copyWith(void Function(Monster) updates) => super.copyWith((message) => updates(message as Monster));
  $pb.BuilderInfo get info_ => _i;
  static Monster create() => Monster();
  Monster createEmptyInstance() => create();
  static $pb.PbList<Monster> createRepeated() => $pb.PbList<Monster>();
  static Monster getDefault() => _defaultInstance ??= create()..freeze();
  static Monster _defaultInstance;

  $core.int get uniqueId => $_get(0, 0);
  set uniqueId($core.int v) { $_setSignedInt32(0, v); }
  $core.bool hasUniqueId() => $_has(0);
  void clearUniqueId() => clearField(1);

  CrossServerInt get monsterId => $_getN(1);
  set monsterId(CrossServerInt v) { setField(2, v); }
  $core.bool hasMonsterId() => $_has(1);
  void clearMonsterId() => clearField(2);

  CrossServerString get name => $_getN(2);
  set name(CrossServerString v) { setField(3, v); }
  $core.bool hasName() => $_has(2);
  void clearName() => clearField(3);

  MonsterType get type1 => $_getN(3);
  set type1(MonsterType v) { setField(4, v); }
  $core.bool hasType1() => $_has(3);
  void clearType1() => clearField(4);

  MonsterType get type2 => $_getN(4);
  set type2(MonsterType v) { setField(5, v); }
  $core.bool hasType2() => $_has(4);
  void clearType2() => clearField(5);

  MonsterType get type3 => $_getN(5);
  set type3(MonsterType v) { setField(6, v); }
  $core.bool hasType3() => $_has(5);
  void clearType3() => clearField(6);

  $core.List<Awakening> get awakenings => $_getList(6);

  $core.List<Awakening> get superAwakenings => $_getList(7);
}

