<?php
// define
$GONDRA_LIST = array(); // ゴンドラリスト
$MEMBER_LIST = array(); // 順番待ちリスト
$BOARDING_LIST = array(); // 各ゴンドラ毎に乗った人数を格納

// データを取得
list ($MAX_GONDRA, $MAX_GROUP) = explode(' ', trim(fgets(STDIN)));
// 乗車数リストを初期化する
for ($i=0; $i < $MAX_GONDRA; $i++) {
    $BOARDING_LIST[$i] = 0;
}

$index = 0;
while (($line = fgets(STDIN)) !== false ) {
    if ($index < $MAX_GONDRA) {
        // ゴンドラリストを作成
        array_push($GONDRA_LIST, $line);
    } else {
        // 順番待ちリストを作成
        array_push($MEMBER_LIST, $line);
    }
    $index++;
}
/* debug
print_r($GONDRA_LIST);
print_r($MEMBER_LIST);
*/

$gondra_index = 0; // ゴンドラ番号
$num = 0; // グループ人数

// グループ人数を取得、全グループ搭乗すれば終了
while ((int)$num = array_shift($MEMBER_LIST)) {
    // 余りの人数を初期化する
    $amari = 0;
    // カウントアップ値を初期化
    $count_up = 0;

    // もしゴンドラ番号が最大なら初期化する
    if ($MAX_GONDRA <= $gondra_index) {
        $gondra_index = 0;
    }

    // ゴンドラを回して乗車人数を取得
    while ((int)$max_num = array_slice($GONDRA_LIST, $gondra_index, 1)[0]) {
        // もし余りの人数が0じゃなければ乗車人数として割り当てる
        if ($amari != 0) {
            $num = $amari;
        }

        // もし乗車人数が全員乗車できない場合
        if ($max_num < $num) {
            // カウントをMAX人数分にする
            $count_up = $max_num;
            // 余剰人数を計算する
            $amari = (int)$num - (int)$max_num;
        } else {
            // ゴンドラ毎のカウントをメンバー人数にする
            $count_up = $num;
            $amari = 0;
        }
        // ゴンドラ毎のカウントを足す
        $BOARDING_LIST[$gondra_index] += (int)$count_up;
        // ゴンドラ番号を次へ
        $gondra_index++;
/* debug
        print_r($BOARDING_LIST);
*/
        // 全員乗車できたので次のグループへ
        if ($amari == 0) {
            break;
        }
    }
}

// ゴンドラ毎の乗車人数を出力する
while ($num = array_shift($BOARDING_LIST)) {
    echo $num . "\n";
}
?>
