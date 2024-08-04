= Timeline Example

//embed[latex]{
% 配列の配列のデータ構造で位置、年月日、テキストを定義し、
% マクロに渡したらタイムラインを生成できるようなマクロを作りたかったが、
% 自分の LaTeX 力が低く時間が掛かりそうだったので諦めた。
% きっともっと良いやり方があると思っている。

% タイムラインを描画
\begin{tikzpicture}[
    event/.style={font=\normalsize, align=left},
    year/.style={font=\bfseries}
]

% タイムラインの垂直線
\draw[thick] (0,0) -- (0,-5);

% タイムラインエントリの追加
\timelineentry{0}{2020}{ああああ}
\timelineentry{1}{2021}{いいいい}
\timelineentry{2}{2022}{うううう}
\timelineentry{3}{2023}{ええええ}
\timelineentry{4}{2024}{おおおお}

\end{tikzpicture}
//}
