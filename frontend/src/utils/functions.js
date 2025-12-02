import { TypeDictList, AttackBonus, items } from './dictionaries.js';

export function calcTypeMult(attack, gen, defT1, defT2) {
  let type1Mult = 1;
  let type2Mult = 1;
  let type1Dict = null;
  let type2Dict = null;

  // Handle Generation 1 type adjustments
  if (gen === 1) {
    if (
      defT1 === 'Fire' ||
      defT1 === 'Poison' ||
      defT1 === 'Psychic' ||
      defT1 === 'Bug'
    ) {
      defT1 = defT1 + 'G1';
    }

    if (
      defT2 === 'Fire' ||
      defT2 === 'Poison' ||
      defT2 === 'Psychic' ||
      defT2 === 'Bug'
    ) {
      defT2 = defT2 + 'G1';
    }
  }

  // Handle Generation 2 Steel type adjustment
  if (gen === 2) {

    if (defT1 === 'Steel') {
      defT1 = 'SteelG2';
    }
    
    if (defT2 === 'Steel') {
      defT2 = 'SteelG2';
    }
  }

  type1Dict = TypeDictList[defT1];
  type1Mult = type1Dict[attack];

  if (defT2 !== '') {
    type2Dict = TypeDictList[defT2];
    type2Mult = type2Dict[attack];
  }

  const totMult = type1Mult * type2Mult;
  return totMult;
}

export function calcSelfMult(
  selfType1,
  selfType2,
  moveType,
  attackBoost,
  item,
  gen
) {
  let stab = 1;

  // Calculate STAB (Same Type Attack Bonus)
  if (selfType1 === moveType || selfType2 === moveType) {
    stab = 1.5;
  }

  const atkBoost = AttackBonus[attackBoost];

  let itemDmg = 1;

  if (item === 'Type Enhancer') {

    if (gen <= 3) {
      itemDmg = items['Type_enhance']['Gen 3-'];
    } else if (gen > 3) {
      itemDmg = items['Type_enhance']['Gen 4+'];
    }

  } else if (item === 'Plate') {
    itemDmg = items['Plate'];

  } else if (item === 'Gem') {
    
    if (gen === 5) {
      itemDmg = items['Gem']['Gen 5'];
    } else {
      itemDmg = items['Gem']['Other Gens'];
    }
  }

  const selfMult = stab * atkBoost * itemDmg;
  return selfMult;
}
