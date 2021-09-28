import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

function Square(props) {
  const className = "square " + (props.winSquare ? "winSquare" : "");
  return (
    <button className={className} onClick={props.onClick}>
      {props.value}
    </button>
  );
}

class Board extends React.Component {
  renderSquare(i, winner) {
    const winSquare = winner ? winner.includes(i) : false;
    return (
      <Square
        value={this.props.squares[i]}
        onClick={() => this.props.onClick(i)}
        winSquare={winSquare}
      />
    );
  }

  render() {
    let myBoard = [];
    for (let i = 0; i < 3; i++) {
      let myRow = [];
      for (let j = 0; j < 3; j++) {
        myRow.push(this.renderSquare(i * 3 + j, this.props.winner));
      }
      myBoard.push(<div className="board-row">{myRow}</div>);
    }
    return <div>{myBoard}</div>;
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      history: [{ squares: Array(9).fill(null), currentMove: null }],
      xIsNext: true,
      stepNumber: 0,
      ascendingSort: true,
    };
  }
  handleClick(i) {
    const history = this.state.history.slice(0, this.state.stepNumber + 1);
    const current = history[history.length - 1];
    const squares = current.squares.slice();
    if (squares[i] || CaculateWinner(squares)) {
      return;
    }

    squares[i] = this.state.xIsNext ? "X" : "O";
    this.setState({
      history: history.concat([{ squares: squares, currentMove: i }]),
      xIsNext: !this.state.xIsNext,
      stepNumber: history.length,
    });
  }
  jump(step) {
    this.setState({
      stepNumber: step,
      xIsNext: step % 2 === 0,
    });
  }
  handle_SortButtonClick() {
    this.setState({
      ascendingSort: !this.state.ascendingSort,
    });
  }
  render() {
    let status;
    const history = this.state.history;
    const current = history[this.state.stepNumber];

    const curentMove = this.state.currentMove;
    const stepNumber = this.state.stepNumber;
    // /const squares = history[history.length - 1].squares;
    const winner = CaculateWinner(current.squares);
    if (winner) {
      status = "The winner is: " + current.squares[winner[0]];
    } else {
      if (stepNumber === 9) {
        status = "GAME IS DRAW";
      } else {
        status = "Next player: " + (this.state.xIsNext ? "X" : "O");
      }
    }
    const moves = history.map((step, move) => {
      const currentMove = step.currentMove;
      const row = parseInt(currentMove / 3);
      const col = currentMove % 3;
      const decs = move
        ? `Go to ${move} step at (${row}, ${col})`
        : "Go to game start";

      const className = move === stepNumber ? "selected" : "";

      return (
        <li key={move}>
          <button onClick={() => this.jump(move)} className={className}>
            {decs}
          </button>
        </li>
      );
    });

    const ascendingSort = this.state.ascendingSort;

    const sort = ascendingSort ? "Descending" : "Ascending";
    console.log(sort);
    return (
      <div className="game">
        <div className="game-board">
          <Board
            squares={current.squares}
            onClick={(i) => this.handleClick(i)}
            winner={winner}
          />
        </div>
        <div className="game-info">
          <div>{status}</div>
          {ascendingSort ? <ol>{moves}</ol> : <ol>{moves.reverse()}</ol>}
        </div>
        <div>
          <button
            className="sortButton"
            onClick={() => this.handle_SortButtonClick()}
          >
            {sort}
          </button>
        </div>
      </div>
    );
  }
}

function CaculateWinner(squares) {
  const winnerBoards = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let i = 0; i < winnerBoards.length; i++) {
    const [a, b, c] = winnerBoards[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return [a, b, c];
    }
  }
  return null;
}

// ========================================

ReactDOM.render(<Game />, document.getElementById("root"));
