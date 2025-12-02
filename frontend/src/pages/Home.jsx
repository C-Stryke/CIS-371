import { useState } from 'react';
import { Types, AttackBonus } from '../utils/dictionaries.js';
import { calcTypeMult, calcSelfMult } from '../utils/functions.js';
import '../App.css';

function Home() {
  const [team, setTeam] = useState(
    Array(6)
      .fill(null)
      .map(() => ({
        type1: '',
        type2: '',
      }))
  );

  const [selectedPokemon, setSelectedPokemon] = useState(0);
  const [selectingType, setSelectingType] = useState(null);

  // Battle calculator state
  const [moveType, setMoveType] = useState('');
  const [generation, setGeneration] = useState(9);
  const [enemyType1, setEnemyType1] = useState('');
  const [enemyType2, setEnemyType2] = useState('');
  const [attackBoost, setAttackBoost] = useState('0');
  const [item, setItem] = useState('');
  const [damageMultiplier, setDamageMultiplier] = useState(null);

  const selectableTypes = Types.filter((type) => type !== '');
  const attackBoostOptions = Object.keys(AttackBonus);
  const itemOptions = ['', 'Type Enhancer', 'Plate', 'Gem'];
  const generations = [1, 2, 3, 4, 5, 6, 7, 8, 9];

  const handleTypeSelect = (type) => {
    const newTeam = [...team];
    newTeam[selectedPokemon] = {
      ...newTeam[selectedPokemon],
      [selectingType]: type,
    };
    setTeam(newTeam);
    setSelectingType(null);
  };

  const handlePokemonSelect = (index) => {
    setSelectedPokemon(index);
    setSelectingType(null);
  };

  const calculateDamage = () => {
    const currentPokemon = team[selectedPokemon];

    if (!currentPokemon.type1 && !currentPokemon.type2) {
      alert('Select at least one type for your attacking Pokemon!');
      return;
    }

    if (!moveType) {
      alert('Select a move type!');
      return;
    }

    if (!enemyType1 && !enemyType2) {
      alert('Select at least one type for the defending Pokemon!');
      return;
    }

    const typeTotal = calcTypeMult(
      moveType,
      generation,
      enemyType1,
      enemyType2
    );

    const selfTotal = calcSelfMult(
      currentPokemon.type1,
      currentPokemon.type2,
      moveType,
      attackBoost,
      item,
      generation
    );
    const total = typeTotal * selfTotal;

    setDamageMultiplier(total);
  };

  const currentPokemon = team[selectedPokemon];

  return (
    <div className='app'>
      <header className='header'>
        <h1>Pokemon Damage Calculator</h1>
        <p className='subtitle'>
          Calculate type effectiveness and damage multipliers
        </p>
      </header>

      <div className='team-container'>
        <h2>Your Team</h2>
        <div className='team-grid'>
          {team.map((pokemon, index) => (
            <div
              key={index}
              className={`pokemon-slot ${
                selectedPokemon === index ? 'active' : ''
              }`}
              onClick={() => handlePokemonSelect(index)}
            >
              <div className='pokemon-number'>#{index + 1}</div>
              <div className='pokemon-types'>
                {pokemon.type1 && (
                  <span className={`type-badge ${pokemon.type1.toLowerCase()}`}>
                    {pokemon.type1}
                  </span>
                )}
                {pokemon.type2 && (
                  <span className={`type-badge ${pokemon.type2.toLowerCase()}`}>
                    {pokemon.type2}
                  </span>
                )}
                {!pokemon.type1 && !pokemon.type2 && (
                  <span className='empty-slot'>Empty</span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className='calculator-section'>
        <div className='left-panel'>
          <div className='editor-container'>
            <h2>Attacking Pokemon #{selectedPokemon + 1}</h2>

            <div className='type-selection'>
              <div className='type-display'>
                <div className='type-row'>
                  <label>Primary Type:</label>
                  <button
                    className='select-type-btn'
                    onClick={() => setSelectingType('type1')}
                  >
                    {currentPokemon.type1 || 'Select Type'}
                  </button>
                </div>
                <div className='type-row'>
                  <label>Secondary Type:</label>
                  <button
                    className='select-type-btn'
                    onClick={() => setSelectingType('type2')}
                  >
                    {currentPokemon.type2 || 'Select Type'}
                  </button>
                </div>
              </div>

              {selectingType && (
                <div className='type-picker'>
                  <h3>
                    Select {selectingType === 'type1' ? 'Primary' : 'Secondary'}{' '}
                    Type
                  </h3>
                  <div className='type-grid'>
                    <button
                      className='type-button clear-button'
                      onClick={() => handleTypeSelect('')}
                    >
                      Clear
                    </button>
                    {selectableTypes.map((type) => (
                      <button
                        key={type}
                        className={`type-button ${type.toLowerCase()}`}
                        onClick={() => handleTypeSelect(type)}
                      >
                        {type}
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>

          <div className='editor-container'>
            <h2>Battle Setup</h2>

            <div className='battle-options'>
              <div className='option-row'>
                <label>Move Type:</label>
                <select
                  value={moveType}
                  onChange={(e) => setMoveType(e.target.value)}
                  className='select-input'
                >
                  <option value=''>Select Move Type</option>
                  {selectableTypes.map((type) => (
                    <option key={type} value={type}>
                      {type}
                    </option>
                  ))}
                </select>
              </div>

              <div className='option-row'>
                <label>Generation:</label>
                <select
                  value={generation}
                  onChange={(e) => setGeneration(Number(e.target.value))}
                  className='select-input'
                >
                  {generations.map((gen) => (
                    <option key={gen} value={gen}>
                      Gen {gen}
                    </option>
                  ))}
                </select>
              </div>

              <div className='option-row'>
                <label>Attack Boost:</label>
                <select
                  value={attackBoost}
                  onChange={(e) => setAttackBoost(e.target.value)}
                  className='select-input'
                >
                  {attackBoostOptions.map((boost) => (
                    <option key={boost} value={boost}>
                      {boost === '0' ? 'No Boost (0)' : boost}
                    </option>
                  ))}
                </select>
              </div>

              <div className='option-row'>
                <label>Item:</label>
                <select
                  value={item}
                  onChange={(e) => setItem(e.target.value)}
                  className='select-input'
                >
                  <option value=''>None</option>
                  {itemOptions
                    .filter((i) => i !== '')
                    .map((itemName) => (
                      <option key={itemName} value={itemName}>
                        {itemName}
                      </option>
                    ))}
                </select>
              </div>
            </div>
          </div>
        </div>

        <div className='right-panel'>
          <div className='editor-container'>
            <h2>Defending Pokemon</h2>

            <div className='enemy-selection'>
              <div className='option-row'>
                <label>Primary Type:</label>
                <select
                  value={enemyType1}
                  onChange={(e) => setEnemyType1(e.target.value)}
                  className='select-input'
                >
                  <option value=''>Select Type</option>
                  {selectableTypes.map((type) => (
                    <option key={type} value={type}>
                      {type}
                    </option>
                  ))}
                </select>
              </div>

              <div className='option-row'>
                <label>Secondary Type:</label>
                <select
                  value={enemyType2}
                  onChange={(e) => setEnemyType2(e.target.value)}
                  className='select-input'
                >
                  <option value=''>Select Type</option>
                  {selectableTypes.map((type) => (
                    <option key={type} value={type}>
                      {type}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <button className='calculate-button' onClick={calculateDamage}>
              Calculate Damage Multiplier
            </button>

            {damageMultiplier !== null && (
              <div className='result-display'>
                <h3>Total Damage Multiplier</h3>
                <div className='multiplier-value'>
                  {damageMultiplier.toFixed(2)}x
                </div>
                <div className='effectiveness'>
                  {damageMultiplier === 0 && 'No Effect!'}
                  {damageMultiplier > 0 &&
                    damageMultiplier < 0.5 &&
                    'Very Weak'}
                  {damageMultiplier >= 0.5 &&
                    damageMultiplier < 1 &&
                    'Not Very Effective'}
                  {damageMultiplier === 1 && 'Normal Damage'}
                  {damageMultiplier > 1 &&
                    damageMultiplier <= 2 &&
                    'Effective!'}
                  {damageMultiplier > 2 &&
                    damageMultiplier <= 4 &&
                    'Super Effective!'}
                  {damageMultiplier > 4 && 'Extremely Effective!'}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
