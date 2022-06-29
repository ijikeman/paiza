<?php
list($MAX_MASU, $MAX_TIMES) = explode(' ', trim(fgets(STDIN)));

//Set マスDATA
$MASU_DATA=array('x');
for ($i=0; $i < ($MAX_MASU-2); $i++) {
    $MASU_DATA[] = trim(fgets(STDIN));
}
$MASU_DATA[] = 'x';

$point = 0; // 現在地
$TIME=0; // サイコロ回数

// サイコロフル
while(($SAI = trim(fgets(STDIN))) != FALSE ) {
    // サイコロカウントアップ
    $TIME++;

    // 移動
    $point+=$SAI;

        // ゴールに到達していた場合は出力して終了
    if (($point+1) >= $MAX_MASU) {
        echo "goal\n$TIME\n";
        exit(0);
    }

    // 止まった場所の効果を反映
    switch(array_slice($MASU_DATA, $point, 1)[0]) {
        case "x": // 何もしない
            break;
        case "-": // 1マス戻る(1以上)
            if ($point > 0) {
                $point--;
            }
            break;
        case "+": // 1マス進む
            $point++;
            break;
        case "r":
            $point=0;
            break; // スタートに戻る
    }
    // 効果によってゴールに到達した場合は終了
    if (($point+1) >= $MAX_MASU) {
        echo "goal\n$TIME\n";
        exit(0);
    }
}
// ゴールしていない場合はstillと現在地を出力
echo "still\n$point\n";
?>
